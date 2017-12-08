from client import *

def registerSelf():
    """
    Using send and recv functionalities, a node can gain access to a network.
    it will be required to deliver a form of identification to prove that it 
    is eleigible to be added to the network
    """
    passcode = 'dummy_password'
    regAdd = '127.0.0.1'
    regPort = 9999
    sock = initSocket('SOCK_STREAM')
    sock = connectNode(sock, regAdd, regPort)

    msg = "Register"
    sendMessage(sock, msg)
    reply = recvMessage(sock)
    print (msg, reply)
    return 0

registerSelf()
