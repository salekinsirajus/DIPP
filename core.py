import signal
import socket
import os

from payloadParser import res
from parser import method_parser

def sig_func(signum, frame):
    pid, status = os.wait()
    print ("Child {pid} terminated with status {status}"
            "\n".format(pid=pid, status = status)
    )


def handle_request(client_connection):
    # BUFFER_SIZE = 1024
    print ("comes to handle_Request")
    while True:
        req_raw = client_connection.recv(1024)
        print ("raw msg recvd ", req_raw)
        req_decoded = req_raw.decode('utf-8')
        print (req_decoded)
        res_raw = method_parser(req_decoded)
        print ("in handle req returned from method parser ",res_raw)
#        if req_decoded == "exit":
#            break
#        res_raw = res(req_decoded)
#        print ("from res() function ",res_raw)
        res_encoded = res_raw.encode('utf-8')
        client_connection.sendall(res_encoded)
    client_connection.close()
    return

def listen_tcp(HOST, PORT):
    #HOST = '127.0.0.1' # localhost
    #PORT = 9999 # some port
    REQ_Q_SIZE = 5; # How many clients are on the queue

    # Initialize and bind a TCP stream to a port and localhost
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Reuse the address immediately after the socket is closed
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Takes a tuple of (host, port) address
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(REQ_Q_SIZE)
    print ("listening on port {}".format(PORT))

    signal.signal(signal.SIGCHLD, sig_func)

    while True:
        client_conn, client_addr = listen_socket.accept()
        # Spawning a child process
        pid = os.fork()
        if pid == 0:
            listen_socket.close()
            handle_request(client_conn) 
            client_conn.close()
            os._exit(0)
        else:
            client_conn.close()

def listen_udp(HOST, PORT):
    # Make a global variable for when to kill the listening port
    # initiate a UDP socket
    sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # reuse this address
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    # bind
    sock.bind((HOST, PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        print ("recvd message", data)
        # print (addr)
        sender_addr = (addr[0], addr[1])
        # decode recvd data
        msg_decoded = data.decode('utf-8')
        print (msg_decoded)
        # In case of PAK, there will be a response.
        # otherwise, it will return certain flag so we won't
        # send any response 
        ack = method_parser (msg_decoded)
        while ack != None:
            ack_encoded = ack.encode('utf-8')
            print ("Sending reply", ack_encoded)
            sock.sendto(ack_encoded, addr)
            break
        print ("end of the loop")

if __name__ == '__main__':
    host = '127.0.0.1'
    tcp_port = 9999
    udp_port = 9998
    listen_tcp(host, tcp_port)
    listen_udp(host, udp_port
