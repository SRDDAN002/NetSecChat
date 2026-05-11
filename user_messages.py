import msgpack # Install with: pip install msgpack
import socket
import random

# = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.connect(('csc4026z.link', 51825))
#sock.send(msgpack.packb({'session': 1, 'request_type':3, 'request_handle': random.randint(0, 2**32 - 1)}))
#data, addr = sock.recvfrom(4096)
#print(msgpack.unpackb(data))

# This will return an error saying "Session not found", because you're not logged in yet. That confirms the server is active.

"""CONNECT_REQUEST"""
def CONNECT_REQUEST():
    return {
        'request_type' : 1, 
        'request_handle': random.randint(0, 2**32 - 1)
        }


"""CONNECT_RESPONSE-->REQUEST_TYPE = 24"""
def CONNECT_RESPONSE(data):
    session = data['session']
    welcome = data['message']
    username = data['username']
    return session, welcome, username

"""PING_REQUEST"""
def PING_REQUEST(session):
    return {
        'request_type':3,
        'session': session,
        'request_handle': random.randint(0, 2**32 - 1)

    }

"""PING_RESPONSE-->REQUEST_TYPE = 23"""
def PING_RESPONSE(data):
    session = data['session']
    #inlcude response handle?
    return data

"""DISCONNECT_REQUEST"""
def DISCONNECT_REQUEST(session):
    return {
        'request_type' : 2,
        'session' : session,
        'request_handle': random.randint(0, 2**32 - 1)
    }

"""DISCONNECT_RESPONSE-->REPONSE TYPE = 23"""
def DISCONNECT_RESPONSE(data):
    message = data['message']
    return message

"""oOK RESPONSE-->RESPONSE TYPE = 21"""
def OK_response():
     #will do this later. seems a bit redundant now because every request has a response
     return "OK from server"

"""ERROR_REPONSE-->RESPONSE TYPE = 20"""
def ERROR_response(data):
     error = data['error']
     return error

"""SERVER_RESPONSE-->RESPONSE TYPE = 36"""
def SERVER_message_RESPONSE(data):
     server_mssg = data['message']
     return server_mssg

"""SET_USERNAME_RESPONSE"""
def SET_USERNAME_REQUEST(session, new_username):
    return {
        'request_type':  13,
        'session': session,
        'request_handle': random.randint(0, 2**32 - 1),
        'username': new_username
    }

"""SET_USERNAME_RESPONSE--> REQUEST TYPE 34"""
def SET_USERNAME_RESPONSE(data):
    old_username = data['old_username']
    new_username = data['new_username']
    return old_username, new_username
    

"""USER_LIST_REQUEST"""
#separate message for listing users in a specific channel?
def USER_LIST(session):
    return {
        'request_type': 14,
        'session': session,
        'request_handle': random.randint(0, 2**32 - 1)
    }

"""USER_LIST_RESPONSE"""
def USER_LIST_RESPONSE(data):
    users = data['users']
    next_page =  data['next_page']
    return users, next_page

"""WHOAMI_REQUEST"""
def WHOAMI_REQUEST(session):
    return {
        'request_type': 11,
        'session': session,
        'request_handle': random.randint(0, 2**32 - 1)
    }

"""WHOAMI_RESPONSE-->REQUEST TYPE = 32"""
def WHOAMI_RESPONSE(data):
    username = data['username']
    return username

def WHOIS_REQUEST(session, username):
    return {
        'request_type': 10,
        'session': session,
        'request_handle': random.randint(0, 2**32 - 1),
        'username': username
    }

"""WHOIS_RESPONSE-->REQUEST TYPE = 31"""
def WHOIS_RESPONSE(data):
    username = data['username']
    channels = data['channels']
    transport = data['transport']
    wireguard_PK = data['wireguard_public_key']
    return username, channels, transport, wireguard_PK



    

    
    







 
    
