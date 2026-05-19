# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        # self.actionSettings = QAction(MainWindow)
        # self.actionSettings.setObjectName(u"actionSettings")
        # self.actionNewChannel = QAction(MainWindow)
        # self.actionNewChannel.setObjectName(u"actionNewChannel")
        # self.actionJoinChannel = QAction(MainWindow)
        # self.actionJoinChannel.setObjectName(u"actionJoinChannel")
        # self.actionLeaveChannel = QAction(MainWindow)
        # self.actionLeaveChannel.setObjectName(u"actionLeaveChannel")
        # self.actionSendDM = QAction(MainWindow)
        # self.actionSendDM.setObjectName(u"actionSendDM")
        # self.actionAbout = QAction(MainWindow)
        # self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.topPanel = QFrame(self.centralwidget)
        self.topPanel.setObjectName(u"topPanel")
        self.topPanel.setFrameShape(QFrame.StyledPanel)
        self.topPanel.setFrameShadow(QFrame.Raised)
        self.topLayout = QHBoxLayout(self.topPanel)
        self.topLayout.setObjectName(u"topLayout")
        self.connectionIndicator = QLabel(self.topPanel)
        self.connectionIndicator.setObjectName(u"connectionIndicator")

        self.topLayout.addWidget(self.connectionIndicator)

        self.connectButton = QPushButton(self.topPanel)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setMaximumWidth(100)

        self.topLayout.addWidget(self.connectButton)

        self.serverInput = QLineEdit(self.topPanel)
        self.serverInput.setObjectName(u"serverInput")
        self.serverInput.setMaximumWidth(150)

        self.topLayout.addWidget(self.serverInput)

        self.usernameLabel = QLabel(self.topPanel)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.topLayout.addWidget(self.usernameLabel)

        self.usernameInput = QLineEdit(self.topPanel)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setMaximumWidth(150)

        self.topLayout.addWidget(self.usernameInput)

        self.horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer1)

        self.sessionIndicator = QLabel(self.topPanel)
        self.sessionIndicator.setObjectName(u"sessionIndicator")

        self.topLayout.addWidget(self.sessionIndicator)


        self.mainLayout.addWidget(self.topPanel)

        self.mainSplitter = QSplitter(self.centralwidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Horizontal)
        self.leftTabWidget = QTabWidget(self.mainSplitter)
        self.leftTabWidget.setObjectName(u"leftTabWidget")
        self.leftTabWidget.setMinimumWidth(250)
        self.leftTabWidget.setMaximumWidth(350)
        self.channelsTab = QWidget()
        self.channelsTab.setObjectName(u"channelsTab")
        self.channelsLayout = QVBoxLayout(self.channelsTab)
        self.channelsLayout.setObjectName(u"channelsLayout")
        self.channelsHeader = QLabel(self.channelsTab)
        self.channelsHeader.setObjectName(u"channelsHeader")

        self.channelsLayout.addWidget(self.channelsHeader)

        self.channelsList = QListWidget(self.channelsTab)
        self.channelsList.setObjectName(u"channelsList")
        self.channelsList.setAlternatingRowColors(False)

        self.channelsLayout.addWidget(self.channelsList)

        self.channelsButtonLayout = QHBoxLayout()
        self.channelsButtonLayout.setObjectName(u"channelsButtonLayout")
        self.createChannelButton = QPushButton(self.channelsTab)
        self.createChannelButton.setObjectName(u"createChannelButton")

        self.channelsButtonLayout.addWidget(self.createChannelButton)

        self.joinChannelButton = QPushButton(self.channelsTab)
        self.joinChannelButton.setObjectName(u"joinChannelButton")

        self.channelsButtonLayout.addWidget(self.joinChannelButton)

        self.leaveChannelButton = QPushButton(self.channelsTab)
        self.leaveChannelButton.setObjectName(u"leaveChannelButton")

        self.channelsButtonLayout.addWidget(self.leaveChannelButton)


        self.channelsLayout.addLayout(self.channelsButtonLayout)

        self.leftTabWidget.addTab(self.channelsTab, "")
        self.usersTab = QWidget()
        self.usersTab.setObjectName(u"usersTab")
        self.usersLayout = QVBoxLayout(self.usersTab)
        self.usersLayout.setObjectName(u"usersLayout")
        self.usersHeader = QLabel(self.usersTab)
        self.usersHeader.setObjectName(u"usersHeader")

        self.usersLayout.addWidget(self.usersHeader)

        self.usersList = QListWidget(self.usersTab)
        self.usersList.setObjectName(u"usersList")
        self.usersList.setAlternatingRowColors(False)

        self.usersLayout.addWidget(self.usersList)

        self.usersButtonLayout = QHBoxLayout()
        self.usersButtonLayout.setObjectName(u"usersButtonLayout")
        self.sendDMButton = QPushButton(self.usersTab)
        self.sendDMButton.setObjectName(u"sendDMButton")

        self.usersButtonLayout.addWidget(self.sendDMButton)

        self.userInfoButton = QPushButton(self.usersTab)
        self.userInfoButton.setObjectName(u"userInfoButton")

        self.usersButtonLayout.addWidget(self.userInfoButton)


        self.usersLayout.addLayout(self.usersButtonLayout)

        self.leftTabWidget.addTab(self.usersTab, "")
        self.mainSplitter.addWidget(self.leftTabWidget)
        self.centerPanel = QWidget(self.mainSplitter)
        self.centerPanel.setObjectName(u"centerPanel")
        self.centerLayout = QVBoxLayout(self.centerPanel)
        self.centerLayout.setObjectName(u"centerLayout")
        self.centerLayout.setContentsMargins(0, 0, 0, 0)
        self.messageDisplay = QPlainTextEdit(self.centerPanel)
        self.messageDisplay.setObjectName(u"messageDisplay")
        self.messageDisplay.setReadOnly(True)

        self.centerLayout.addWidget(self.messageDisplay)

        self.messageInputFrame = QFrame(self.centerPanel)
        self.messageInputFrame.setObjectName(u"messageInputFrame")
        self.messageInputLayout = QHBoxLayout(self.messageInputFrame)
        self.messageInputLayout.setObjectName(u"messageInputLayout")
        self.messageInput = QLineEdit(self.messageInputFrame)
        self.messageInput.setObjectName(u"messageInput")

        self.messageInputLayout.addWidget(self.messageInput)

        self.sendMessageButton = QPushButton(self.messageInputFrame)
        self.sendMessageButton.setObjectName(u"sendMessageButton")
        self.sendMessageButton.setMaximumWidth(80)

        self.messageInputLayout.addWidget(self.sendMessageButton)


        self.centerLayout.addWidget(self.messageInputFrame)

        self.mainSplitter.addWidget(self.centerPanel)
        self.rightTabWidget = QTabWidget(self.mainSplitter)
        self.rightTabWidget.setObjectName(u"rightTabWidget")
        self.rightTabWidget.setMinimumWidth(250)
        self.rightTabWidget.setMaximumWidth(350)
        self.channelInfoTab = QWidget()
        self.channelInfoTab.setObjectName(u"channelInfoTab")
        self.channelInfoLayout = QVBoxLayout(self.channelInfoTab)
        self.channelInfoLayout.setObjectName(u"channelInfoLayout")
        self.channelInfoHeader = QLabel(self.channelInfoTab)
        self.channelInfoHeader.setObjectName(u"channelInfoHeader")

        self.channelInfoLayout.addWidget(self.channelInfoHeader)

        self.channelNameDisplay = QLabel(self.channelInfoTab)
        self.channelNameDisplay.setObjectName(u"channelNameDisplay")
        self.channelNameDisplay.setWordWrap(True)

        self.channelInfoLayout.addWidget(self.channelNameDisplay)

        self.channelDescLabel = QLabel(self.channelInfoTab)
        self.channelDescLabel.setObjectName(u"channelDescLabel")

        self.channelInfoLayout.addWidget(self.channelDescLabel)

        self.channelDescription = QPlainTextEdit(self.channelInfoTab)
        self.channelDescription.setObjectName(u"channelDescription")
        self.channelDescription.setReadOnly(True)
        self.channelDescription.setMaximumHeight(100)

        self.channelInfoLayout.addWidget(self.channelDescription)

        self.channelMembersLabel = QLabel(self.channelInfoTab)
        self.channelMembersLabel.setObjectName(u"channelMembersLabel")

        self.channelInfoLayout.addWidget(self.channelMembersLabel)

        self.channelMembersList = QListWidget(self.channelInfoTab)
        self.channelMembersList.setObjectName(u"channelMembersList")
        self.channelMembersList.setMaximumHeight(150)

        self.channelInfoLayout.addWidget(self.channelMembersList)

        self.rightTabWidget.addTab(self.channelInfoTab, "")
        self.userInfoTab = QWidget()
        self.userInfoTab.setObjectName(u"userInfoTab")
        self.userInfoLayout = QVBoxLayout(self.userInfoTab)
        self.userInfoLayout.setObjectName(u"userInfoLayout")
        self.userInfoHeader = QLabel(self.userInfoTab)
        self.userInfoHeader.setObjectName(u"userInfoHeader")

        self.userInfoLayout.addWidget(self.userInfoHeader)

        self.userNameDisplay = QLabel(self.userInfoTab)
        self.userNameDisplay.setObjectName(u"userNameDisplay")

        self.userInfoLayout.addWidget(self.userNameDisplay)

        self.userStatusLabel = QLabel(self.userInfoTab)
        self.userStatusLabel.setObjectName(u"userStatusLabel")

        self.userInfoLayout.addWidget(self.userStatusLabel)

        self.userStatusDisplay = QLabel(self.userInfoTab)
        self.userStatusDisplay.setObjectName(u"userStatusDisplay")

        self.userInfoLayout.addWidget(self.userStatusDisplay)

        self.userBioLabel = QLabel(self.userInfoTab)
        self.userBioLabel.setObjectName(u"userBioLabel")

        self.userInfoLayout.addWidget(self.userBioLabel)

        self.userBioDisplay = QPlainTextEdit(self.userInfoTab)
        self.userBioDisplay.setObjectName(u"userBioDisplay")
        self.userBioDisplay.setReadOnly(True)

        self.userInfoLayout.addWidget(self.userBioDisplay)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.userInfoLayout.addItem(self.verticalSpacer)

        self.rightTabWidget.addTab(self.userInfoTab, "")
        self.mainSplitter.addWidget(self.rightTabWidget)

        self.mainLayout.addWidget(self.mainSplitter)

        self.bottomPanel = QFrame(self.centralwidget)
        self.bottomPanel.setObjectName(u"bottomPanel")
        self.bottomPanel.setFrameShape(QFrame.StyledPanel)
        self.bottomPanel.setFrameShadow(QFrame.Raised)
        self.bottomLayout = QHBoxLayout(self.bottomPanel)
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.statusMessage = QLabel(self.bottomPanel)
        self.statusMessage.setObjectName(u"statusMessage")

        self.bottomLayout.addWidget(self.statusMessage)

        self.horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bottomLayout.addItem(self.horizontalSpacer2)

        self.messageCount = QLabel(self.bottomPanel)
        self.messageCount.setObjectName(u"messageCount")

        self.bottomLayout.addWidget(self.messageCount)


        self.mainLayout.addWidget(self.bottomPanel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuChat = QMenu(self.menubar)
        self.menuChat.setObjectName(u"menuChat")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuChat.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionDisconnect)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        # self.menuEdit.addAction(self.actionSettings)
        # self.menuChat.addAction(self.actionNewChannel)
        # self.menuChat.addAction(self.actionJoinChannel)
        # self.menuChat.addAction(self.actionLeaveChannel)
        # self.menuChat.addSeparator()
        # self.menuChat.addAction(self.actionSendDM)
        # self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SIGNAL NETWORK // COMMUNICATION INTERFACE v1.0", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"/* ===== NEON COLOR PALETTE (CUSTOMIZE HERE) ===== */\n"
"QMainWindow {\n"
" background-color: #0A0E27;\n"
" color: #39FF14;\n"
"}\n"
"\n"
"QWidget {\n"
" background-color: #0A0E27;\n"
" color: #39FF14;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: Tab Styling ===== */\n"
"QTabWidget::pane {\n"
" border: 2px solid #FF6B1A;\n"
" background-color: #0A0E27;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
" background-color: #1A1F3A;\n"
" color: #39FF14;\n"
" padding: 8px 20px;\n"
" border: 1px solid #FF6B1A;\n"
" margin-right: 2px;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
" background-color: #FF6B1A;\n"
" color: #0A0E27;\n"
" border: 2px solid #39FF14;\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
" background-color: #2A2F4A;\n"
" border: 1px solid #39FF14;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: Button Styling (Retro 3D Effect) ===== */\n"
"QPushButton {\n"
" background-color: #1A1F3A;\n"
" color: #39FF14;\n"
" border: 2px outset #FF6B1A;\n"
" padding: 6px 12px"
                        ";\n"
" border-radius: 0px;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
" font-size: 10pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: #2A2F4A;\n"
" color: #FF9500;\n"
" border: 2px outset #39FF14;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" border-style: inset;\n"
" background-color: #0A0E27;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: Input Field Styling (CRT-like) ===== */\n"
"QLineEdit, QTextEdit, QPlainTextEdit {\n"
" background-color: #0F1430;\n"
" color: #39FF14;\n"
" border: 1px solid #FF6B1A;\n"
" padding: 4px;\n"
" font-family: 'Courier New', monospace;\n"
" font-size: 10pt;\n"
" selection-background-color: #FF6B1A;\n"
" selection-color: #0A0E27;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {\n"
" border: 2px solid #39FF14;\n"
" background-color: #1A1F3A;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: List and Tree View Styling ===== */\n"
"QListWidget, QTreeWidget, QTableWidget {\n"
" background-color: #0F1430;\n"
" color: #39FF14;\n"
" border: 1px sol"
                        "id #FF6B1A;\n"
" gridline-color: #FF6B1A;\n"
" font-family: 'Courier New', monospace;\n"
"}\n"
"\n"
"QListWidget::item:selected, QTreeWidget::item:selected, QTableWidget::item:selected {\n"
" background-color: #FF6B1A;\n"
" color: #0A0E27;\n"
"}\n"
"\n"
"QListWidget::item:hover, QTreeWidget::item:hover, QTableWidget::item:hover {\n"
" background-color: #2A2F4A;\n"
" color: #FF9500;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: Scrollbar Styling ===== */\n"
"QScrollBar:vertical {\n"
" background-color: #0A0E27;\n"
" width: 16px;\n"
" border: 1px solid #FF6B1A;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
" background-color: #FF6B1A;\n"
" border-radius: 8px;\n"
" min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
" background-color: #39FF14;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
" background-color: #0A0E27;\n"
" height: 16px;\n"
" border: 1px solid #FF6B1A;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
" background-color: #FF6B1A;\n"
" border-radius: 8px;\n"
" min-width: 20px;\n"
"}\n"
"\n"
""
                        "QScrollBar::handle:horizontal:hover {\n"
" background-color: #39FF14;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: Label Styling ===== */\n"
"QLabel {\n"
" color: #39FF14;\n"
" font-family: 'Courier New', monospace;\n"
"}\n"
"\n"
"QLabel[status=\"active\"] {\n"
" color: #39FF14;\n"
"}\n"
"\n"
"QLabel[status=\"inactive\"] {\n"
" color: #FF6B1A;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: Menu Bar and Status Bar ===== */\n"
"QMenuBar {\n"
" background-color: #1A1F3A;\n"
" color: #39FF14;\n"
" border-bottom: 2px solid #FF6B1A;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
" background-color: #FF6B1A;\n"
" color: #0A0E27;\n"
"}\n"
"\n"
"QMenu {\n"
" background-color: #1A1F3A;\n"
" color: #39FF14;\n"
" border: 2px solid #FF6B1A;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
" background-color: #FF6B1A;\n"
" color: #0A0E27;\n"
"}\n"
"\n"
"QStatusBar {\n"
" background-color: #1A1F3A;\n"
" color: #39FF14;\n"
" border-top: 2px solid #FF6B1A;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: Separator/Divider ===== */\n"
"QFrame[frameShape=\"4\"] {\n"
""
                        " border-color: #FF6B1A;\n"
"}\n"
"\n"
"/* ===== CUSTOMIZABLE: Splitter Styling ===== */\n"
"QSplitter::handle {\n"
" background-color: #1A1F3A;\n"
" border-left: 1px solid #FF6B1A;\n"
" border-right: 1px solid #FF6B1A;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
" background-color: #2A2F4A;\n"
"}\n"
"   ", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect to Server", None))
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        # self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        # self.actionNewChannel.setText(QCoreApplication.translate("MainWindow", u"Create Channel", None))
        # self.actionJoinChannel.setText(QCoreApplication.translate("MainWindow", u"Join Channel", None))
        # self.actionLeaveChannel.setText(QCoreApplication.translate("MainWindow", u"Leave Channel", None))
        # self.actionSendDM.setText(QCoreApplication.translate("MainWindow", u"Send Direct Message", None))
        # self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.topPanel.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QFrame {\n"
" background-color: #1A1F3A;\n"
" border-bottom: 2px solid #FF6B1A;\n"
" padding: 8px;\n"
"}\n"
"      ", None))
        self.connectionIndicator.setText(QCoreApplication.translate("MainWindow", u"[\u25cf\u25cf\u25cf] NETWORK STATUS", None))
        self.connectionIndicator.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #39FF14;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
"}\n"
"         ", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"\u25ba CONNECT", None))
        self.serverInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"localhost:8000", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"[USER]", None))
        self.usernameLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
"}\n"
"         ", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter username", None))
        self.sessionIndicator.setText(QCoreApplication.translate("MainWindow", u"\u25c4 SESSION ACTIVE", None))
        self.sessionIndicator.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #39FF14;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
"}\n"
"         ", None))
        self.channelsHeader.setText(QCoreApplication.translate("MainWindow", u"\u250c\u2500 AVAILABLE CHANNELS \u2500\u2510", None))
        self.channelsHeader.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
" padding: 4px;\n"
"}\n"
"          ", None))
        self.createChannelButton.setText(QCoreApplication.translate("MainWindow", u"\u271a CREATE", None))
        self.joinChannelButton.setText(QCoreApplication.translate("MainWindow", u"\u2192 JOIN", None))
        self.leaveChannelButton.setText(QCoreApplication.translate("MainWindow", u"\u2190 LEAVE", None))
        self.leftTabWidget.setTabText(self.leftTabWidget.indexOf(self.channelsTab), QCoreApplication.translate("MainWindow", u"\u25c6 CHANNELS", None))
        self.usersHeader.setText(QCoreApplication.translate("MainWindow", u"\u250c\u2500 CONNECTED USERS \u2500\u2510", None))
        self.usersHeader.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
" padding: 4px;\n"
"}\n"
"          ", None))
        self.sendDMButton.setText(QCoreApplication.translate("MainWindow", u"\u2709 DM", None))
        self.userInfoButton.setText(QCoreApplication.translate("MainWindow", u"\u24d8 INFO", None))
        self.leftTabWidget.setTabText(self.leftTabWidget.indexOf(self.usersTab), QCoreApplication.translate("MainWindow", u"\u25c8 USERS", None))
        self.messageDisplay.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QPlainTextEdit {\n"
" background-color: #0F1430;\n"
" color: #39FF14;\n"
" border: 2px solid #FF6B1A;\n"
" padding: 8px;\n"
" font-family: 'Courier New', monospace;\n"
" font-size: 10pt;\n"
"}\n"
"         ", None))
        self.messageInputFrame.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QFrame {\n"
" background-color: #1A1F3A;\n"
" border-top: 2px solid #FF6B1A;\n"
" padding: 8px;\n"
"}\n"
"         ", None))
        self.messageInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TYPE MESSAGE [ENTER TO SEND]", None))
        self.sendMessageButton.setText(QCoreApplication.translate("MainWindow", u"\u25ba SEND", None))
        self.channelInfoHeader.setText(QCoreApplication.translate("MainWindow", u"\u250c\u2500 CHANNEL DETAILS \u2500\u2510", None))
        self.channelInfoHeader.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
" padding: 4px;\n"
"}\n"
"          ", None))
        self.channelNameDisplay.setText(QCoreApplication.translate("MainWindow", u"[CHANNEL NAME]", None))
        self.channelNameDisplay.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #39FF14;\n"
" font-weight: bold;\n"
" padding: 4px;\n"
"}\n"
"          ", None))
        self.channelDescLabel.setText(QCoreApplication.translate("MainWindow", u"DESCRIPTION:", None))
        self.channelDescLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
"}\n"
"          ", None))
        self.channelMembersLabel.setText(QCoreApplication.translate("MainWindow", u"MEMBERS:", None))
        self.channelMembersLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
"}\n"
"          ", None))
        self.rightTabWidget.setTabText(self.rightTabWidget.indexOf(self.channelInfoTab), QCoreApplication.translate("MainWindow", u"\u25c6 CH INFO", None))
        self.userInfoHeader.setText(QCoreApplication.translate("MainWindow", u"\u250c\u2500 USER DETAILS \u2500\u2510", None))
        self.userInfoHeader.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
" padding: 4px;\n"
"}\n"
"          ", None))
        self.userNameDisplay.setText(QCoreApplication.translate("MainWindow", u"[USERNAME]", None))
        self.userNameDisplay.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #39FF14;\n"
" font-weight: bold;\n"
" padding: 4px;\n"
"}\n"
"          ", None))
        self.userStatusLabel.setText(QCoreApplication.translate("MainWindow", u"STATUS:", None))
        self.userStatusLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
"}\n"
"          ", None))
        self.userStatusDisplay.setText(QCoreApplication.translate("MainWindow", u"\u25cf ONLINE", None))
        self.userStatusDisplay.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #39FF14;\n"
" padding: 4px;\n"
"}\n"
"          ", None))
        self.userBioLabel.setText(QCoreApplication.translate("MainWindow", u"BIO/INFO:", None))
        self.userBioLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
"}\n"
"          ", None))
        self.rightTabWidget.setTabText(self.rightTabWidget.indexOf(self.userInfoTab), QCoreApplication.translate("MainWindow", u"\u25c8 USR INFO", None))
        self.bottomPanel.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QFrame {\n"
" background-color: #1A1F3A;\n"
" border-top: 2px solid #FF6B1A;\n"
" padding: 4px 8px;\n"
"}\n"
"      ", None))
        self.statusMessage.setText(QCoreApplication.translate("MainWindow", u"\u2524 READY \u251c", None))
        self.statusMessage.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #39FF14;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
"}\n"
"         ", None))
        self.messageCount.setText(QCoreApplication.translate("MainWindow", u"MSG: 0 | USERS: 0 | CHANNELS: 0", None))
        self.messageCount.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"QLabel {\n"
" color: #FF6B1A;\n"
" font-weight: bold;\n"
" font-family: 'Courier New', monospace;\n"
"}\n"
"         ", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"FILE", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.menuChat.setTitle(QCoreApplication.translate("MainWindow", u"CHAT", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"HELP", None))
    # retranslateUi

