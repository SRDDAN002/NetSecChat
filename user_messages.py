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


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('csc4026z.link', 51825))
    #very wonky but this is just to test
    keyboard = input(f"Welcome to a little test!\nOptions:\n1. CONNECT\n2. DISCONNECT\n3. CHANGE USERNAME\n4. USER LIST\n5. WHOAMI\n6. WHOIS\n")
    if keyboard == "1":
    #connect
        sock.send(msgpack.packb(CONNECT_REQUEST()))
        data, addr = sock.recvfrom(4096)
        data = msgpack.unpackb(data)
        session, welcome, username = CONNECT_RESPONSE(data)
        print(f"{welcome} IP address {addr[0]} at port number {addr[1]}\n Username is {username}")  
    keyboard = input(f"Options:\n1. CONNECT\n2. DISCONNECT\n3. CHANGE USERNAME\n4. USER LIST\n5. WHOAMI\n6. WHOIS\n")
    #need to continuosly receive and send pings
    while (keyboard != "2"):
        if keyboard == "3":
            new_username = input(f"Enter you new username: \n")
            sock.send(msgpack.packb(SET_USERNAME_REQUEST(session, new_username)))
            data, addr = sock.recvfrom(4096)
            data = msgpack.unpackb(data)
            if data['response_type'] != 20:
                old_username, new_username = SET_USERNAME_RESPONSE(data)
                print(f"{old_username} changed to {new_username}")  
                username = new_username
            else:
                error = ERROR_response(data)
                print(f"An error has ocurred: {error}")

        if keyboard == "4":
            sock.send(msgpack.packb(USER_LIST(session)))
            data, addr = sock.recvfrom(4096)
            data = msgpack.unpackb(data)
            if data['response_type'] != 20:
                user_list, next_page_bool = USER_LIST_RESPONSE(data)
                print(f"User list: {user_list}\n Any additional pages is {next_page_bool}")  
            else:
                error = ERROR_response(data)
                print(f"An error has ocurred: {error}")

        if keyboard == "5":
            sock.send(msgpack.packb(WHOAMI_REQUEST(session)))
            data, addr = sock.recvfrom(4096)
            data = msgpack.unpackb(data)
            if data['response_type'] != 20:
                username_query = WHOAMI_RESPONSE(data)
                print(f"It would seem you have forgotten who you are. Your name is {username_query} and you are welcome here!!!")  
            else:
                error = ERROR_response(data)
                print(f"An error has ocurred: {error}")
            
        if keyboard == '6':
            identity = input (f"It seems you're curious. Who are we spying on?\n")
            sock.send(msgpack.packb(WHOIS_REQUEST(session, identity)))
            data, addr = sock.recvfrom(4096)
            data = msgpack.unpackb(data)
            if data['response_type'] != 20:
                username_spy, channels, transport, wireguard_key = WHOIS_RESPONSE(data)
                print(f"{username_spy} belongs to {channels} channels. The transport method is {transport} and the key is {wireguard_key}")  
            else:
                error = ERROR_response(data)
                print(f"An error has ocurred: {error}")
        keyboard = input(f"Options:\n1. CONNECT\n2. DISCONNECT\n3. CHANGE USERNAME\n4. USER LIST\n5. WHOAMI\n6. WHOIS\n")

         
    sock.send(msgpack.packb(DISCONNECT_REQUEST(session)))
    data, addr = sock.recvfrom(4096)
    data = msgpack.unpackb(data)
    goodbye = DISCONNECT_RESPONSE(data)
    print(f"{goodbye} from IP address {addr[0]} at port number {addr[1]}\n Username {username} is now terminated")  




if '__name__ == __main__':
    main()

 
    
