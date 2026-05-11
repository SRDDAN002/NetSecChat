import msgpack # Install with: pip install msgpack
import socket
import random
from channel_msg import *
from user_messages import *
from session_msg import *


class User:
    def __init__(self):
        pass
class Session:
    def __init__(self,data):
        self.session, _, _ = CONNECT_RESPONSE(data)
    
    
class Connection:
    def __init__(self,ip,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((ip, port))
        
    def connect(self):
        
        self.sock.send(msgpack.packb(CONNECT_REQUEST()))
        data, addr = self.sock.recvfrom(4096)
        data = msgpack.unpackb(data)
        self.session, welcome, username = CONNECT_RESPONSE(data)
        print(f"{welcome} IP address {addr[0]} at port number {addr[1]}\n Username is {username}") 
    
    def getSession(self):
        return self.session
    
class Message:
    def __init__(self):
        pass
class Channel:
    def __init__(self):
        pass
    
class Server:
    def __init__(self):
        pass
    
    
        