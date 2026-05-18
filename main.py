import asyncio
import sys
from typing import Optional

import msgpack
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QThread, Signal, Slot

from ui_form import Ui_MainWindow
from classes import Connection, Message
from channel_msg import *
from user_messages import *
from session_msg import *


class NetworkWorker(QtCore.QObject):
    """Handles all async networking operations in a separate thread."""
    
    # Signals for UI updates
    status_message = Signal(str)
    connected = Signal(bool)
    data_received = Signal(str, object)  # (operation_type, data)
    error_occurred = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.server: Optional[Connection] = None
        self.loop: Optional[asyncio.AbstractEventLoop] = None
        self.thread: Optional[QThread] = None
    
    def setup_worker_thread(self):
        """Setup the worker to run in a separate thread."""
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.initialize_event_loop)
        self.thread.start()
    
    @Slot()
    def initialize_event_loop(self):
        """Initialize asyncio event loop for this thread."""
        try:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            self.status_message.emit("Event loop initialized")
        except Exception as e:
            self.error_occurred.emit(f"Failed to initialize event loop: {str(e)}")
    
    @Slot()
    def connect_to_server(self):
        """Connect to the server."""
        if self.loop:
            asyncio.run_coroutine_threadsafe(self._async_connect(), self.loop)
    
    async def _async_connect(self):
        """Async connection logic."""
        try:
            from classes import Connection
            self.server = Connection('csc4026z.link', 51825)
            connect_msg = {"request_type": 1}
            data = self.server.connect(connect_msg)
            self.connected.emit(True)
            self.status_message.emit(f"Connected! Session: {self.server.getSession()}")
            self.data_received.emit("connected", data)
        except Exception as e:
            self.connected.emit(False)
            self.error_occurred.emit(f"Connection failed: {str(e)}")
    
    @Slot()
    def disconnect_from_server(self):
        """Disconnect from the server."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_disconnect(), self.loop)
    
    async def _async_disconnect(self):
        """Async disconnection logic."""
        try:
            data = await self.server.disconnect()
            goodbye = data.get("message", "Disconnected")
            self.connected.emit(False)
            self.status_message.emit(f"{goodbye}")
            self.server = None
        except Exception as e:
            self.error_occurred.emit(f"Disconnection failed: {str(e)}")
    
    @Slot(str)
    def set_username(self, new_username: str):
        """Set a new username."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(
                self._async_set_username(new_username), self.loop
            )
    
    async def _async_set_username(self, new_username: str):
        """Async set username."""
        try:
            msg = {"request_type": 3, "username": new_username}
            data = await self.server.send(msg)
            self.status_message.emit(f"Username changed to: {new_username}")
            self.data_received.emit("username_changed", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to change username: {str(e)}")
    
    @Slot(bool)
    def list_users(self, filter_channel: bool = False, channel_name: str = ""):
        """List users, optionally filtered by channel."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(
                self._async_list_users(filter_channel, channel_name), self.loop
            )
    
    async def _async_list_users(self, filter_channel: bool, channel_name: str):
        """Async list users."""
        try:
            if filter_channel and channel_name:
                msg = {"request_type": 4, "channel": channel_name}
            else:
                msg = {"request_type": 4}
            data = await self.server.send(msg)
            self.status_message.emit("User list retrieved")
            self.data_received.emit("user_list", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to list users: {str(e)}")
    
    @Slot(str)
    def whoami(self):
        """Get current username."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_whoami(), self.loop)
    
    async def _async_whoami(self):
        """Async whoami."""
        try:
            msg = {"request_type": 5}
            data = await self.server.send(msg)
            self.status_message.emit(f"You are: {data}")
            self.data_received.emit("whoami", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to get username: {str(e)}")
    
    @Slot(str)
    def search_user(self, identity: str):
        """Search for a user."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_search_user(identity), self.loop)
    
    async def _async_search_user(self, identity: str):
        """Async search user."""
        try:
            msg = {"request_type": 6, "identity": identity}
            data = await self.server.send(msg)
            self.status_message.emit(f"Search results for {identity}")
            self.data_received.emit("search_user", data)
        except Exception as e:
            self.error_occurred.emit(f"Search failed: {str(e)}")
    
    @Slot(str, str)
    def create_channel(self, channel_name: str, description: str):
        """Create a new channel."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(
                self._async_create_channel(channel_name, description), self.loop
            )
    
    async def _async_create_channel(self, channel_name: str, description: str):
        """Async create channel."""
        try:
            msg = {"request_type": 7, "channel_name": channel_name, "description": description}
            data = await self.server.send(msg)
            self.status_message.emit(f"Channel '{channel_name}' created")
            self.data_received.emit("channel_created", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to create channel: {str(e)}")
    
    @Slot()
    def list_channels(self):
        """List all channels."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_list_channels(), self.loop)
    
    async def _async_list_channels(self):
        """Async list channels."""
        try:
            msg = {"request_type": 8}
            data = await self.server.send(msg)
            self.status_message.emit("Channels list retrieved")
            self.data_received.emit("channel_list", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to list channels: {str(e)}")
    
    @Slot(str)
    def channel_info(self, channel_name: str):
        """Get channel information."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_channel_info(channel_name), self.loop)
    
    async def _async_channel_info(self, channel_name: str):
        """Async get channel info."""
        try:
            msg = {"request_type": 9, "channel_name": channel_name}
            data = await self.server.send(msg)
            self.status_message.emit(f"Channel info: {channel_name}")
            self.data_received.emit("channel_info", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to get channel info: {str(e)}")
    
    @Slot(str)
    def join_channel(self, channel_name: str):
        """Join a channel."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_join_channel(channel_name), self.loop)
    
    async def _async_join_channel(self, channel_name: str):
        """Async join channel."""
        try:
            msg = {"request_type": 10, "channel_name": channel_name}
            data = await self.server.send(msg)
            self.status_message.emit(f"Joined channel: {channel_name}")
            self.data_received.emit("channel_joined", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to join channel: {str(e)}")
    
    @Slot(str)
    def leave_channel(self, channel_name: str):
        """Leave a channel."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_leave_channel(channel_name), self.loop)
    
    async def _async_leave_channel(self, channel_name: str):
        """Async leave channel."""
        try:
            msg = {"request_type": 11, "channel_name": channel_name}
            data = await self.server.send(msg)
            self.status_message.emit(f"Left channel: {channel_name}")
            self.data_received.emit("channel_left", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to leave channel: {str(e)}")
    
    @Slot(str, str)
    def send_channel_message(self, channel_name: str, message_text: str):
        """Send a message to a channel."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(
                self._async_send_channel_message(channel_name, message_text), self.loop
            )
    
    async def _async_send_channel_message(self, channel_name: str, message_text: str):
        """Async send channel message."""
        try:
            msg_obj = Message(message_text)
            msg = {
                "request_type": 12,
                "channel_name": channel_name,
                "message": msg_obj.data,
            }
            data = await self.server.send(msg)
            self.status_message.emit(f"Message sent to {channel_name}")
            self.data_received.emit("message_sent", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to send message: {str(e)}")
    
    @Slot(str, str)
    def send_user_message(self, username: str, message_text: str):
        """Send a direct message to a user."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(
                self._async_send_user_message(username, message_text), self.loop
            )
    
    async def _async_send_user_message(self, username: str, message_text: str):
        """Async send user message."""
        try:
            msg = {"request_type": 13, "username": username, "message": message_text}
            data = await self.server.send(msg)
            self.status_message.emit(f"Direct message sent to {username}")
            self.data_received.emit("user_message_sent", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to send user message: {str(e)}")
    
    def cleanup(self):
        """Cleanup worker thread."""
        if self.loop:
            self.loop.call_soon_threadsafe(self.loop.stop)
        if self.thread:
            self.thread.quit()
            self.thread.wait()


class MainWindow(QtWidgets.QMainWindow):
    """Main application window using Ui_MainWindow template."""
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize the network worker
        self.worker = NetworkWorker()
        self.worker.setup_worker_thread()
        
        # Setup UI (add custom widgets to the template)
        self.setup_custom_ui()
        
        # Connect signals and slots
        self.connect_signals_slots()
        
        # Window settings
        self.setWindowTitle("NetSecChat")
        self.resize(900, 700)
    
    def setup_custom_ui(self):
        """Setup custom UI elements within the template."""
        # Create a central layout for the main content
        layout = QtWidgets.QVBoxLayout()
        
        # Welcome label
        self.welcomeLbl = QtWidgets.QLabel(
            "Welcome to NetSecChat!\n\nSelect an option below:", 
            alignment=QtCore.Qt.AlignCenter
        )
        welcome_font = self.welcomeLbl.font()
        welcome_font.setPointSize(14)
        self.welcomeLbl.setFont(welcome_font)
        layout.addWidget(self.welcomeLbl)
        
        # Text display area
        self.textDisplay = QtWidgets.QPlainTextEdit()
        self.textDisplay.setReadOnly(False)
        self.textDisplay.setPlaceholderText("Operation output will appear here...")
        layout.addWidget(self.textDisplay)
        
        # Buttons container
        buttons_layout = QtWidgets.QGridLayout()
        
        self.con = QtWidgets.QPushButton("Connect")
        self.disCon = QtWidgets.QPushButton("Disconnect")
        self.changeUname = QtWidgets.QPushButton("Change Username")
        self.listUsers = QtWidgets.QPushButton("List Users")
        self.whoIs = QtWidgets.QPushButton("Search User")
        self.whoAmI = QtWidgets.QPushButton("Who Am I")
        self.createChannel = QtWidgets.QPushButton("Create Channel")
        self.listChannels = QtWidgets.QPushButton("List Channels")
        self.joinChannel = QtWidgets.QPushButton("Join Channel")
        self.leaveChannel = QtWidgets.QPushButton("Leave Channel")
        self.sendChannelMsg = QtWidgets.QPushButton("Send Channel Message")
        self.sendUserMsg = QtWidgets.QPushButton("Send Direct Message")
        
        # Arrange buttons in grid
        buttons_layout.addWidget(self.con, 0, 0)
        buttons_layout.addWidget(self.disCon, 0, 1)
        buttons_layout.addWidget(self.whoAmI, 0, 2)
        buttons_layout.addWidget(self.changeUname, 1, 0)
        buttons_layout.addWidget(self.listUsers, 1, 1)
        buttons_layout.addWidget(self.whoIs, 1, 2)
        buttons_layout.addWidget(self.createChannel, 2, 0)
        buttons_layout.addWidget(self.listChannels, 2, 1)
        buttons_layout.addWidget(self.joinChannel, 2, 2)
        buttons_layout.addWidget(self.leaveChannel, 3, 0)
        buttons_layout.addWidget(self.sendChannelMsg, 3, 1)
        buttons_layout.addWidget(self.sendUserMsg, 3, 2)
        
        layout.addLayout(buttons_layout)
        
        # Set the layout to the central widget
        self.ui.centralwidget.setLayout(layout)
    
    def connect_signals_slots(self):
        """Connect button signals to worker slots and worker signals to UI slots."""
        # Button clicks to worker methods
        self.con.clicked.connect(self.worker.connect_to_server)
        self.disCon.clicked.connect(self.worker.disconnect_from_server)
        self.whoAmI.clicked.connect(self.worker.whoami)
        self.listUsers.clicked.connect(lambda: self.worker.list_users(False))
        self.listChannels.clicked.connect(self.worker.list_channels)
        
        # Buttons that need input dialogs
        self.changeUname.clicked.connect(self.on_change_username)
        self.whoIs.clicked.connect(self.on_search_user)
        self.createChannel.clicked.connect(self.on_create_channel)
        self.joinChannel.clicked.connect(self.on_join_channel)
        self.leaveChannel.clicked.connect(self.on_leave_channel)
        self.sendChannelMsg.clicked.connect(self.on_send_channel_message)
        self.sendUserMsg.clicked.connect(self.on_send_user_message)
        
        # Worker signals to UI slots
        self.worker.status_message.connect(self.on_status_message)
        self.worker.connected.connect(self.on_connection_state_changed)
        self.worker.data_received.connect(self.on_data_received)
        self.worker.error_occurred.connect(self.on_error)
    
    # Slot handlers for button clicks that require input
    @Slot()
    def on_change_username(self):
        """Handle change username button."""
        new_username, ok = QtWidgets.QInputDialog.getText(
            self, "Change Username", "Enter new username:"
        )
        if ok and new_username:
            self.worker.set_username(new_username)
    
    @Slot()
    def on_search_user(self):
        """Handle search user button."""
        identity, ok = QtWidgets.QInputDialog.getText(
            self, "Search User", "Enter username to search:"
        )
        if ok and identity:
            self.worker.search_user(identity)
    
    @Slot()
    def on_create_channel(self):
        """Handle create channel button."""
        channel_name, ok = QtWidgets.QInputDialog.getText(
            self, "Create Channel", "Enter channel name:"
        )
        if ok and channel_name:
            description, ok2 = QtWidgets.QInputDialog.getText(
                self, "Create Channel", "Enter channel description:"
            )
            if ok2:
                self.worker.create_channel(channel_name, description)
    
    @Slot()
    def on_join_channel(self):
        """Handle join channel button."""
        channel_name, ok = QtWidgets.QInputDialog.getText(
            self, "Join Channel", "Enter channel name:"
        )
        if ok and channel_name:
            self.worker.join_channel(channel_name)
    
    @Slot()
    def on_leave_channel(self):
        """Handle leave channel button."""
        channel_name, ok = QtWidgets.QInputDialog.getText(
            self, "Leave Channel", "Enter channel name:"
        )
        if ok and channel_name:
            self.worker.leave_channel(channel_name)
    
    @Slot()
    def on_send_channel_message(self):
        """Handle send channel message button."""
        channel_name, ok = QtWidgets.QInputDialog.getText(
            self, "Send Channel Message", "Enter channel name:"
        )
        if ok and channel_name:
            message_text, ok2 = QtWidgets.QInputDialog.getText(
                self, "Send Channel Message", "Enter message:"
            )
            if ok2 and message_text:
                self.worker.send_channel_message(channel_name, message_text)
    
    @Slot()
    def on_send_user_message(self):
        """Handle send direct message button."""
        username, ok = QtWidgets.QInputDialog.getText(
            self, "Send Direct Message", "Enter recipient username:"
        )
        if ok and username:
            message_text, ok2 = QtWidgets.QInputDialog.getText(
                self, "Send Direct Message", "Enter message:"
            )
            if ok2 and message_text:
                self.worker.send_user_message(username, message_text)
    
    # Worker signal handlers
    @Slot(str)
    def on_status_message(self, message: str):
        """Handle status messages from worker."""
        self.ui.statusbar.showMessage(message, 5000)
        self.textDisplay.appendPlainText(f"[STATUS] {message}")
    
    @Slot(bool)
    def on_connection_state_changed(self, connected: bool):
        """Handle connection state changes."""
        self.con.setEnabled(not connected)
        self.disCon.setEnabled(connected)
        # Enable other buttons only when connected
        self.changeUname.setEnabled(connected)
        self.listUsers.setEnabled(connected)
        self.whoIs.setEnabled(connected)
        self.whoAmI.setEnabled(connected)
        self.createChannel.setEnabled(connected)
        self.listChannels.setEnabled(connected)
        self.joinChannel.setEnabled(connected)
        self.leaveChannel.setEnabled(connected)
        self.sendChannelMsg.setEnabled(connected)
        self.sendUserMsg.setEnabled(connected)
    
    @Slot(str, object)
    def on_data_received(self, operation_type: str, data: object):
        """Handle data received from worker."""
        self.textDisplay.appendPlainText(f"\n[{operation_type.upper()}]\n{str(data)}\n")
    
    @Slot(str)
    def on_error(self, error_msg: str):
        """Handle errors from worker."""
        self.textDisplay.appendPlainText(f"\n[ERROR] {error_msg}\n")
        QtWidgets.QMessageBox.critical(self, "Error", error_msg)
    
    def closeEvent(self, event):
        """Handle window close event."""
        self.worker.cleanup()
        event.accept()


def main():
    """Main application entry point."""
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    

    
