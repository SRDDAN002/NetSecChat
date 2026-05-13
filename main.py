import asyncio

import msgpack # Install with: pip install msgpack
import socket
import random
from channel_msg import *
from user_messages import *
from session_msg import *

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.con = QtWidgets.QPushButton("Connect")  
        self.disCon = QtWidgets.QPushButton("Disconnect")
        self.changeUname = QtWidgets.QPushButton("Change Username")
        self.listUsers = QtWidgets.QPushButton("List Users")
        self.whoIs = QtWidgets.QPushButton("Search User")   
        self.whoAmI = QtWidgets.QPushButton("Username")

        self.welcomeLbl = QtWidgets.QLabel("Welcome to NetSac! \n Options:", alignment = QtCore.Qt.AlignCenter)
        
        self.layout.addWidget(self.welcomeLbl, 0, 2)

        self.innerContainer = QtWidgets.QWidget()
        self.subLayout = QtWidgets.QHBoxLayout(self.innerContainer)

        self.textDisplay = QtWidgets.QPlainTextEdit()

        self.subLayout.addWidget(self.textDisplay)
        self.layout.addWidget(self.innerContainer, 1, 2)

        self.layout.addWidget(self.whoIs, 2, 1)
        self.layout.addWidget(self.con, 2, 2)
        self.layout.addWidget(self.changeUname, 2, 3)
        self.layout.addWidget(self.listUsers, 3, 1)
        self.layout.addWidget(self.disCon, 3, 2)
        self.layout.addWidget(self.whoAmI, 3, 3)

        self.con.clicked.connect(self.magic)

    

def main():

    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('csc4026z.link', 51825))

    # if widget.con.clicked()

    #very wonky but this is just to test
    keyboard = input(loop_text)
    while (keyboard != "2"):
        
        if keyboard == "3":
            
            new_username = input(f"Enter you new username: ")
            
            data = await server.set_username(new_username)
            
            

        if keyboard == "4":
            
            channel = input(f"Filter by channel [Y\\N]?")
            if channel == "N":
                data = await server.user_list_pro()
                
                
            elif channel =="Y":
                filter_channel = input("channel name:\n")
                data =await server.user_list_pro(filter_channel)
                
            else:
                print("Invalid input")
                
            

        if keyboard == "5":
            data = await server.whoami()
            
        if keyboard == '6':
            identity = input (f"It seems you're curious. Who are we spying on?\n")
            data = await server.whosis(identity)
        
        if keyboard =="7":
            
            channel_name = input("Channel name:")
            description = input("Description:")
            await server.CHANNEL_CREATE(channel_name,description)

        if keyboard =="8":
            
            print(await server.CHANNEL_LIST_PRO())

        if keyboard =="9":
            
            channel_name = input("Channel name:")
            await server.CHANNEL_INFO(channel_name)

        if keyboard =="10":
            
            channel_name = input("Channel name:")
            await server.CHANNEL_JOIN(channel_name)

        if keyboard =="11":
            
            channel_name = input("Channel name:")
            await server.CHANNEL_LEAVE(channel_name)

            #TODO
        if keyboard =="12":
            
            channel_name = input("Channel name:")
            msg = input("Message:")
            msg = Message(msg)
            msg = msg.data
            await server.CHANNEL_MESSAGE(channel_name,msg)
        keyboard = input(loop_text)
        
        if keyboard == "13":
            username = input("Send message to ?")
            msg = input("message?")
            data = await server.user_message(username,msg)
        
            
  
    #goodbye = DISCONNECT_RESPONSE()
    data = await server.disconnect()
    #print(data)
    goodbye = data["message"]
    print(f"{goodbye} from IP address {server.connection.ip} at port number {server.connection.port}\n Username {server.getUsername()} is now terminated")  




if '__name__ == __main__':
    main()
    
