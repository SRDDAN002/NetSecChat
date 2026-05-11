import msgpack # Install with: pip install msgpack
import socket
import random

# = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.connect(('csc4026z.link', 51825))
#sock.send(msgpack.packb({'session': 1, 'request_type':3, 'request_handle': random.randint(0, 2**32 - 1)}))
#data, addr = sock.recvfrom(4096)
#print(msgpack.unpackb(data))

"""CHANNEL_CREATE """
def CHANNEL_CREATE(sock,session,channel_name,description=""):
    data= msgpack.packb({
        "request_type":4,               # request_type u8
        "session":session,         # u32
        "request_handle":random.randint(0, 2**32 - 1),  # u32
        "channel":channel_name,    # s[20]
        "description":description      # s[100]
    })
    sock.send(data)
    
    data, addr = sock.recvfrom(4096)
    data = msgpack.unpackb(data)
    
    response_type = data["response_type"]
    session = data["session"]
    #response_handle = data["response_handle"]
    channel = data["channel"]    # Name of new channel
    description = data["description"]        # A description associated with the new Channel
    
    
    return response_type,channel,description

"""CHANNEL_LIST"""
def CHANNEL_LIST(sock,session,offset=0):
    data= msgpack.packb({
        "request_type":5,               # request_type u8
        "session":session,         # u32
        "request_handle":random.randint(0, 2**32 - 1),  # u32
        "offset":offset
    })    
    sock.send(data)
    data, addr = sock.recvfrom(4096)
    data = msgpack.unpackb(data)
    
    response_type = data["response_type"]
    session = data["session"]
    response_handle = data["response_handle"]
    channels = data["channels"]    # Name of new channel
    next_page = data["next_page"]        # A description associated with the new Channel
    
    return data

"""CHANNEL_LIST_PRO"""
def CHANNEL_LIST_PRO(sock,session,offset=0):  
    i =0
    channels = CHANNEL_LIST(sock,session,offset)["channels"]
    next_page = CHANNEL_LIST(sock,session,offset)["next_page"]
    if next_page:
        offset =10
        while next_page and i<10: # i is to limit incase recussion depth exceeded , can be removed if confident code works
            i+=1
            tmp_channels = CHANNEL_LIST(sock,session,offset)["channels"]
            next_page = CHANNEL_LIST(sock,session,offset)["next_page"]
            channels+=tmp_channels
            offset+=10

   # response_type = data["response_type"]
    #session = data["session"]
    #response_handle = data["response_handle"]
    #channels = data["channels"]    # Name of new channel
    #next_page = data["next_page"]        # A description associated with the new Channel
    
    return channels
    
    
    