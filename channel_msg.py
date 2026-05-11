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
    
    if response_type ==25:
        print(f"Channel \"{channel}\" created")
    else:
        error = data["error"]
        print(f"Error: \"{error}\"")
        return data
    
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
    if response_type ==26:
        channels = data["channels"]
        print(f"List \"{channels}\"")
    else:
        error = data["error"]
        print(f"Error: \"{error}\"")
        return data
    session = data["session"]
    response_handle = data["response_handle"]
    channels = data["channels"]    # Name of new channel
    next_page = data["next_page"]        # A description associated with the new Channel
    
    return data

"""CHANNEL_LIST_PRO"""
def CHANNEL_LIST_PRO(sock,session,offset=0):  
    i =0
    data =CHANNEL_LIST(sock,session,offset)
    channels = data["channels"]
    next_page = data["next_page"]
    if next_page:
        offset =10
        while next_page and i<10: # i is to limit incase recussion depth exceeded , can be removed if confident code works
            i+=1
            data =CHANNEL_LIST(sock,session,offset)
            
            tmp_channels = data["channels"]
            next_page = data["next_page"]
            channels+=tmp_channels
            offset+=10

   # response_type = data["response_type"]
    #session = data["session"]
    #response_handle = data["response_handle"]
    #channels = data["channels"]    # Name of new channel
    #next_page = data["next_page"]        # A description associated with the new Channel
    return channels
    
"""CHANNEL_INFO"""
def CHANNEL_INFO(sock,session,channel           ):
    data= msgpack.packb({
        "request_type":6,               # request_type u8
        "session":session,         # u32
        "request_handle":random.randint(0, 2**32 - 1),  # u32
        "channel":channel
    }) 
    sock.send(data)
    
    data, addr = sock.recvfrom(4096)
    data = msgpack.unpackb(data)
    response_type = data["response_type"]
    if response_type==27:
        channel_name = data["channel"]
    
        description = data["description"]
        channel_members = data["members"]
        print(f"Channel name: \"{channel_name}\"\nDescription: {description}\nChannel members: {channel_members}")
    else:
        error = data["error"]
        print(f"Error: \"{error}\"")
    
    
    
    
    return channel_name,description,channel_members

"""CHANNEL_JOIN"""
def CHANNEL_JOIN(sock,session,channel           ):
    data= msgpack.packb({
        "request_type":7,               # request_type u8
        "session":session,         # u32
        "request_handle":random.randint(0, 2**32 - 1),  # u32
        "channel":channel
    }) 
    sock.send(data)
    
    data, addr = sock.recvfrom(4096)
    data = msgpack.unpackb(data)
    
    response_type = data["response_type"]
    if response_type ==28:
        response_handle = data["response_handle"]
        username = data["username"]
    
        channel_name = data["channel"]
        description = data["description"]
        print(f"Joined \"{channel}\"")
    else:
        
        error = data["error"]
        print(f"Error: \"{error}\"")
        return data
        
    
    
    
    
    
    return response_handle,username,channel_name,description
"""CHANNEL_LEAVE"""
def CHANNEL_LEAVE(sock,session,channel           ):
    data= msgpack.packb({
        "request_type":8,               # request_type u8
        "session":session,         # u32
        "request_handle":random.randint(0, 2**32 - 1),  # u32
        "channel":channel
    }) 
    sock.send(data)
    
    data, addr = sock.recvfrom(4096)
    data = msgpack.unpackb(data)
    
    
    response_type = data["response_type"]
    if response_type ==29:
        print(f"Left \"{channel}\"")
    else:
        error = data["error"]
        print(f"Error: \"{error}\"")
        return data
    response_handle = data["response_handle"]
    username = data["username"]
    channel_name = data["channel"]
    
    
    return response_handle,username,channel_name

"""CHANNEL_MESSAGE"""
def CHANNEL_MESSAGE(sock,session,channel,message):
    data= msgpack.packb({
        "request_type":9,               # request_type u8
        "session":session,         # u32
        "request_handle":random.randint(0, 2**32 - 1),  # u32
        "channel":channel,
        "message":message
    }) 
    sock.send(data)
    
    data, addr = sock.recvfrom(4096)
    data = msgpack.unpackb(data)
    response_type = data["response_type"]
    if response_type ==30:
        print(f"Message sent to channel \"{channel}\"")
    else:
        error = data["error"]
        print(f"Error: \"{error}\"")
        return data
    
    response_handle = data["response_handle"]
    username = data["username"]
    
    channel_name = data["channel"]
    message = data["message"]
    if response_type ==30:
        print(f"Message sent to channel \"{channel}\"")
    else:
        print(f"Failed to send message to channel \"{channel}\"")
        return data
    return response_handle,username,channel_name,message


    