import asyncio
import sys
from typing import Optional
from datetime import datetime

import msgpack
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QThread, Signal, Slot, Qt

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
    users_list_updated = Signal(list)
    channels_list_updated = Signal(list)
    message_received = Signal(str, str)  # (sender, message)
    
    def __init__(self):
        super().__init__()
        self.server: Optional[Connection] = None
        self.loop: Optional[asyncio.AbstractEventLoop] = None
        self.thread: Optional[QThread] = None
        self.username: str = ""
    
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
    
    @Slot(str, str)
    def connect_to_server(self, host: str = "", username: str = ""):
        """Connect to the server."""
        if self.loop:
            asyncio.run_coroutine_threadsafe(
                self._async_connect(host or 'csc4026z.link', 51825, username), self.loop
            )
    
    async def _async_connect(self, host: str, port: int, username: str):
        """Async connection logic."""
        try:
            self.server = Connection(host, port)
            self.username = username
            connect_msg = {"request_type": 1}
            data = self.server.connect(connect_msg)
            self.connected.emit(True)
            self.status_message.emit(f"Connected to {host}:{port} - Session established")
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
            self.username = new_username
            self.status_message.emit(f"Username set to: {new_username}")
            self.data_received.emit("username_changed", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to change username: {str(e)}")
    
    @Slot()
    def list_users(self):
        """List users."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_list_users(), self.loop)
    
    async def _async_list_users(self):
        """Async list users."""
        try:
            msg = {"request_type": 4}
            data = await self.server.send(msg)
            users = data.get("users", []) if isinstance(data, dict) else []
            self.users_list_updated.emit(users)
            self.status_message.emit(f"User list retrieved ({len(users)} users)")
            self.data_received.emit("user_list", data)
        except Exception as e:
            self.error_occurred.emit(f"Failed to list users: {str(e)}")
    
    @Slot()
    def whoami(self):
        """Get current username."""
        if self.loop and self.server:
            asyncio.run_coroutine_threadsafe(self._async_whoami(), self.loop)
    
    async def _async_whoami(self):
        """Async whoami."""
        try:
            msg = {"request_type": 5}
            data = await self.server.send(msg)
            self.status_message.emit(f"Current user: {self.username}")
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
            channels = data.get("channels", []) if isinstance(data, dict) else []
            self.channels_list_updated.emit(channels)
            self.status_message.emit(f"Channels list retrieved ({len(channels)} channels)")
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
            self.message_received.emit(f"[{self.username}@{channel_name}]", message_text)
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
            self.message_received.emit(f"[DM→{username}]", message_text)
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
    """Main application window using Ui_MainWindow from chat_interface.ui"""
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize the network worker
        self.worker = NetworkWorker()
        self.worker.setup_worker_thread()
        
        # Track current channel/user for messaging
        self.current_channel: Optional[str] = None
        self.current_dm_user: Optional[str] = None
        
        # Connect signals and slots
        self.connect_signals_slots()
        
        # Setup menu actions
        self.setup_menu_actions()
    
    def connect_signals_slots(self):
        """Connect button signals to worker slots and worker signals to UI slots."""
        # Top panel
        self.ui.connectButton.clicked.connect(self.on_connect_clicked)
        
        # Channels tab
        self.ui.createChannelButton.clicked.connect(self.on_create_channel)
        self.ui.joinChannelButton.clicked.connect(self.on_join_channel)
        self.ui.leaveChannelButton.clicked.connect(self.on_leave_channel)
        self.ui.channelsList.itemClicked.connect(self.on_channel_selected)
        
        # Users tab
        self.ui.sendDMButton.clicked.connect(self.on_send_dm)
        self.ui.userInfoButton.clicked.connect(self.on_user_info)
        self.ui.usersList.itemClicked.connect(self.on_user_selected)
        
        # Message input
        self.ui.messageInput.returnPressed.connect(self.on_send_message)
        self.ui.sendMessageButton.clicked.connect(self.on_send_message)
        
        # Worker signals to UI slots
        self.worker.status_message.connect(self.on_status_message)
        self.worker.connected.connect(self.on_connection_state_changed)
        self.worker.data_received.connect(self.on_data_received)
        self.worker.error_occurred.connect(self.on_error)
        self.worker.users_list_updated.connect(self.on_users_list_updated)
        self.worker.channels_list_updated.connect(self.on_channels_list_updated)
        self.worker.message_received.connect(self.on_message_received)
    
    def setup_menu_actions(self):
        """Setup menu actions."""
        self.ui.actionConnect.triggered.connect(self.on_connect_clicked)
        self.ui.actionDisconnect.triggered.connect(self.worker.disconnect_from_server)
        self.ui.actionExit.triggered.connect(self.close)
        # self.ui.actionNewChannel.triggered.connect(self.on_create_channel)
        # self.ui.actionJoinChannel.triggered.connect(self.on_join_channel)
        # self.ui.actionLeaveChannel.triggered.connect(self.on_leave_channel)
        # self.ui.actionSendDM.triggered.connect(self.on_send_dm)
        # self.ui.actionAbout.triggered.connect(self.on_about)
    
    # Slot handlers for button clicks
    @Slot()
    def on_connect_clicked(self):
        """Handle connect button."""
        server = self.ui.serverInput.text() or 'csc4026z.link'
        username = self.ui.usernameInput.text() or f"user_{QtCore.QTime.currentTime().hour}{QtCore.QTime.currentTime().minute}"
        
        if not username.strip():
            QtWidgets.QMessageBox.warning(self, "Connection", "Please enter a username")
            return
        
        self.worker.connect_to_server(server, username)
        self.ui.usernameLabel.setText(f"[{username}]")
    
    @Slot()
    def on_create_channel(self):
        """Handle create channel."""
        channel_name, ok = QtWidgets.QInputDialog.getText(
            self, "Create Channel", "Channel name:"
        )
        if ok and channel_name.strip():
            description, ok2 = QtWidgets.QInputDialog.getText(
                self, "Create Channel", "Description:"
            )
            if ok2:
                self.worker.create_channel(channel_name, description or "")
                self.worker.list_channels()
    
    @Slot()
    def on_join_channel(self):
        """Handle join channel."""
        channel_name, ok = QtWidgets.QInputDialog.getText(
            self, "Join Channel", "Channel name:"
        )
        if ok and channel_name.strip():
            self.worker.join_channel(channel_name)
            self.current_channel = channel_name
    
    @Slot()
    def on_leave_channel(self):
        """Handle leave channel."""
        if self.current_channel:
            self.worker.leave_channel(self.current_channel)
            self.current_channel = None
        else:
            QtWidgets.QMessageBox.warning(self, "Leave Channel", "No channel selected")
    
    @Slot()
    def on_send_dm(self):
        """Handle send DM."""
        if self.current_dm_user:
            message = self.ui.messageInput.text()
            if message.strip():
                self.worker.send_user_message(self.current_dm_user, message)
                self.ui.messageInput.clear()
            else:
                QtWidgets.QMessageBox.warning(self, "Send DM", "Message cannot be empty")
        else:
            QtWidgets.QMessageBox.warning(self, "Send DM", "Please select a user first")
    
    @Slot()
    def on_user_info(self):
        """Handle user info."""
        if self.current_dm_user:
            self.worker.search_user(self.current_dm_user)
        else:
            QtWidgets.QMessageBox.warning(self, "User Info", "Please select a user first")
    
    @Slot()
    def on_send_message(self):
        """Handle send message."""
        if self.current_channel:
            message = self.ui.messageInput.text()
            if message.strip():
                self.worker.send_channel_message(self.current_channel, message)
                self.ui.messageInput.clear()
            else:
                QtWidgets.QMessageBox.warning(self, "Send Message", "Message cannot be empty")
        else:
            QtWidgets.QMessageBox.warning(self, "Send Message", "Please select a channel first")
    
    @Slot()
    def on_about(self):
        """Handle about dialog."""
        QtWidgets.QMessageBox.about(
            self,
            "About NetSecChat",
            "NetSecChat v1.0\n\n"
            "A secure network communication interface.\n"
            "Built with PySide6 and retro-futuristic styling.\n\n"
            "© 2026"
        )
    
    # Selection handlers
    @Slot(object)
    def on_channel_selected(self, item):
        """Handle channel selection."""
        self.current_channel = item.text()
        self.ui.messageDisplay.setPlainText(f"[Channel: {self.current_channel}]\n\n")
        self.ui.channelNameDisplay.setText(f"Channel: {self.current_channel}")
    
    @Slot(object)
    def on_user_selected(self, item):
        """Handle user selection."""
        self.current_dm_user = item.text()
        self.ui.messageDisplay.setPlainText(f"[DM with: {self.current_dm_user}]\n\n")
        self.ui.userNameDisplay.setText(f"User: {self.current_dm_user}")
    
    # Worker signal handlers
    @Slot(str)
    def on_status_message(self, message: str):
        """Handle status messages from worker."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.ui.statusMessage.setText(f"[{timestamp}] {message}")
        self.ui.messageDisplay.appendPlainText(f"[STATUS] {message}")
    
    @Slot(bool)
    def on_connection_state_changed(self, connected: bool):
        """Handle connection state changes."""
        self.ui.connectButton.setText("● DISCONNECT" if connected else "► CONNECT")
        self.ui.connectButton.setEnabled(True)
        self.ui.connectionIndicator.setText("●●● CONNECTED" if connected else "●●● OFFLINE")
        self.ui.connectionIndicator.setStyleSheet(
            "QLabel { color: #39FF14; font-weight: bold; }" if connected 
            else "QLabel { color: #FF6B1A; font-weight: bold; }"
        )
        
        # Disable UI elements when disconnected
        self.ui.serverInput.setEnabled(not connected)
        self.ui.usernameInput.setEnabled(not connected)
        self.ui.createChannelButton.setEnabled(connected)
        self.ui.joinChannelButton.setEnabled(connected)
        self.ui.leaveChannelButton.setEnabled(connected)
        self.ui.sendDMButton.setEnabled(connected)
        self.ui.userInfoButton.setEnabled(connected)
        self.ui.messageInput.setEnabled(connected)
        self.ui.sendMessageButton.setEnabled(connected)
        
        if connected:
            self.worker.list_channels()
            self.worker.list_users()
    
    @Slot(str, object)
    def on_data_received(self, operation_type: str, data: object):
        """Handle data received from worker."""
        self.ui.messageDisplay.appendPlainText(f"\n[{operation_type.upper()}]\n{str(data)}\n")
    
    @Slot(str)
    def on_error(self, error_msg: str):
        """Handle errors from worker."""
        self.ui.messageDisplay.appendPlainText(f"\n[ERROR] {error_msg}\n")
        QtWidgets.QMessageBox.critical(self, "Error", error_msg)
    
    @Slot(list)
    def on_users_list_updated(self, users: list):
        """Update users list."""
        self.ui.usersList.clear()
        for user in users:
            self.ui.usersList.addItem(str(user))
        self.ui.messageCount.setText(f"MSG: 0 | USERS: {len(users)} | CHANNELS: 0")
    
    @Slot(list)
    def on_channels_list_updated(self, channels: list):
        """Update channels list."""
        self.ui.channelsList.clear()
        for channel in channels:
            self.ui.channelsList.addItem(str(channel))
        self.ui.messageCount.setText(f"MSG: 0 | USERS: 0 | CHANNELS: {len(channels)}")
    
    @Slot(str, str)
    def on_message_received(self, sender: str, message: str):
        """Handle message received."""
        self.ui.messageDisplay.appendPlainText(f"{sender}: {message}")
    
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
