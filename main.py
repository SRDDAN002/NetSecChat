import msgpack # Install with: pip install msgpack
import socket
import random
from channel_msg import *
from user_messages import *
from session_msg import *
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('csc4026z.link', 51825))
    menu_text = f"Welcome to a little test!\nOptions:\n1. CONNECT\n"
    loop_text = f"""Welcome to a little test!\n
    2. DISCONNECT\n
    3. CHANGE USERNAME\n
    4. USER LIST\n
    5. WHOAMI\n
    6. WHOIS\n
    7.CHANNEL_CREATE\n
    8.CHANNEL_LIST\n
    9.CHANNEL_INFO\n
    10.CHANNEL_JOIN\n
    11.CHANNEL_LEAVE\n
    12.CHANNEL_MSG\n
    """
    #very wonky but this is just to test
    keyboard = input(menu_text)
    if keyboard == "1":
    #connect
        sock.send(msgpack.packb(CONNECT_REQUEST()))
        data, addr = sock.recvfrom(4096)
        data = msgpack.unpackb(data)
        session, welcome, username = CONNECT_RESPONSE(data)
        print(f"{welcome} IP address {addr[0]} at port number {addr[1]}\n Username is {username}")  
    
    #need to continuosly receive and send pings
    while (keyboard != "2"):
        keyboard = input(loop_text)
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
        if keyboard =="7":
            channel_name = input("Channel name:")
            description = input("Description:")
            CHANNEL_CREATE(sock,session,channel_name=channel_name,description=description)
        if keyboard =="8":
            print(CHANNEL_LIST_PRO(sock,session))
        if keyboard =="9":
            channel_name = input("Channel name:")
            
            CHANNEL_INFO(sock,session,channel_name)
        if keyboard =="10":
            channel_name = input("Channel name:")
            
            CHANNEL_JOIN(sock,session,channel_name)
        if keyboard =="11":
            channel_name = input("Channel name:")
            
            CHANNEL_LEAVE(sock,session,channel_name)
        if keyboard =="12":
            channel_name = input("Channel name:")
            msg = input("Message:")
            
            CHANNEL_MESSAGE(sock,session,channel_name,msg)
        
            
        
        
        

         
    sock.send(msgpack.packb(DISCONNECT_REQUEST(session)))
    data, addr = sock.recvfrom(4096)
    data = msgpack.unpackb(data)
    goodbye = DISCONNECT_RESPONSE(data)
    print(f"{goodbye} from IP address {addr[0]} at port number {addr[1]}\n Username {username} is now terminated")  




if '__name__ == __main__':
    main()