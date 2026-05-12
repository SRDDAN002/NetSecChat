import msgpack # Install with: pip install msgpack
import socket
import random
from channel_msg import *
from user_messages import *
from session_msg import *

#TODO
class User:
    def __init__(self):
        self.username = None
        self.channels = None
    def setUsername(self,username):
        self.username = username
    def getUsername(self):
        return self.username
    def channel_msg(self):
        pass
    def dm(self):
        pass
    def my_channels():
        pass
    

    
    
class Connection:
    def __init__(self,ip,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((ip, port))
        self.ip = ip
        self.port = port
    def connect(self):
        
        data = self.send(CONNECT_REQUEST())
        self.session, welcome, username = CONNECT_RESPONSE(data)
        print(f"{welcome} IP address {self.ip} at port number {self.port}\n Username is {username}")
        return self.session, welcome, username  
    
    def getSession(self):
        return self.session
    
    def send(self,data):
        if data["request_type"] !=1:
            data["session"] = self.session
        data["request_handle"]=random.randint(0, 2**32 - 1)
        data = msgpack.packb(data)
        self.sock.send(data)
        data, addr = self.sock.recvfrom(4096)
        data = msgpack.unpackb(data)
        return data
    #TODO
    def disconnect(self):
        data = self.send(DISCONNECT_REQUEST())
        return data
connection = Connection('csc4026z.link', 51825)    
    
class Message:
    def __init__(self,data):
        self.data = data
    def encrypt(self):
        pass
    
class Channel:
    def __init__(self,name):
        self.name = name
        self.members = None
    def getMembers(self):
        self.members = CHANNEL_INFO(self.name)
        return self.members
    def leave(self):
        CHANNEL_LEAVE(self.name)
        #TODO
    def update(self):
        pass
    def getInfo(self):
        return CHANNEL_INFO(self.name)
        
class Server:
    def __init__(self):
        self.channels= None
    def getChannels(self):
        self.channels = CHANNEL_LIST_PRO()
        print(self.channels)
        return self.channels
    def createChannel(self,name,description=""):
        self.channels+= CHANNEL_CREATE(name,description)["channel"]
    def channelInfo(name):
        return CHANNEL_INFO(name)
    def join_channel(self,name):
        self.channels+= CHANNEL_JOIN(name)["channel"]
    def whoIs(self):
        pass
    
    
        