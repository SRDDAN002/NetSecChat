import msgpack # Install with: pip install msgpack
import socket
import random



"""CHANNEL_CREATE_REQUEST """
def CHANNEL_CREATE(session,request_handle,channel_name,description=""):
    return msgpack.packb([
        4,               # request_type u8
        session,         # u32
        request_handle,  # u32
        channel_name,    # s[20]
        description      # s[100]
    ])