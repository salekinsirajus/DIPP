##############################################################################
#
# File: client.py
# Author: Sirajus Salekin
# Usage: ./client.py || python client.py
#
##############################################################################
# UPDATE/TODO:
#
# This is a staructural view of the client program.
# Although we produced a state diagram, we need to 
# make sure if we need states in our program, and if so
# what's the best way to achieve that
#
##############################################################################
#
# Discussion:
# 
# A client can move between a few states = {Registered, connected, disconnected
# everything_else}
# * Registered: has a netID/IP address available
# * Connected: active and part of the network
# * Disconnected: Not connected/power_down, but still part of the network
#
# In a tabular form:
#       +------------+---------+--------------------------------+    
#       |Variables-> |  netID  | 
#       |Statets     |                                           
#       +------------+---------+--------------------------------+
#       |Resgistered |  Valid  |
#       +------------+---------+--------------------------------+
#       |Connected   |  Valid  |
#       +------------+---------+--------------------------------+
#       |Disconnected|  Valid  |
#       +------------+---------+--------------------------------+
#       |None(of abv)| InValid |
#       +------------+---------+--------------------------------+
##############################################################################
#
# Programming Paradigm: Procedural. Using procedural programming style will
# help keep the visibility of the states clear. Secondly, this library would
# written in the simplest form possible, since it will go on a device with a
# small memory and CPU. We will try to keep it short and simple (KISS).
#
# Need to make a list of error and error types
#
##############################################################################
#!/usr/bin/env python
import socket                   # for socket library
# import logging                # for logging events
#from Crypto.Cipher import AES   # for encryption and decryption

def initSocket(service_type):
    """Returns a UDP or TCP socket initialized"""
    valid_services = {'SOCK_STREAM', 'SOCK_DGRAM'}
    while service_type not in valid_services:
        raise ValueError("Invalid stream type. Valid: SOCK_{STREAM, DGRAM}")
        return 1
    try: 
        if service_type is 'SOCK_STREAM':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)           
        # Add a log record here?
        print ("Successfully initialized a {} socket".format(service_type))
    except socket.error as e:
        print ("Socket creation unsuccessfull")
        return e
    return sock


def connectNode(sock, address, port):
    """Return a connection based on the socket, address and port"""
    # If there is no socket, use initSocket to initialize one
    # Check if the socket is closed? Validate the IP and port?
    # Then connect to the address and port
    # If there is not port provided, connect to any port??/default port
    #while socket is None:
    #    print ("The socket provided is empty {}".format(socket))
    print ("Connecting to {0} on port {1}".format(address, port))
    try:
        sock.connect((address, port))
        print ("Succeess connection to {} on port {}".format(address, port))
    except socket.error as e:
        print ("cant connect: {}".format(e))
        exit("Please try again and make sure the server port is listening")
    return sock

def sendMessage(sock, msg):
    # send a message once using the socket provided
    """
    Echo server is an easy task. But how does one send data. For example
    data that needs to be binded with an executable code.
    Or do we care ebout it at this point?
    It can be very general, right now. Send any general data.
    """
    try:
        sock.sendall(msg.encode('utf-8'))
    except Exception as e:
        print ("Message sending error: {}".format(e))
        return 1
    return 0

if __name__ == '__main__':
    tcp = initSocket('SOCK_STREAM')
    udp = initSocket('SOCK_DGRAM')
    s = connectNode(tcp, '127.0.0.1', 9999)
    sendMessage(s, "hello world")
    tcp.close()
    connectNode(udp, '127.0.0.1', 9999)
    udp.close()
   # connectNode("test", tcp, udp)
