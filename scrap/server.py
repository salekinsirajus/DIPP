# Should handle concurrent clients
import signal
import socket
import os
import subprocess

from tmp import res     # temporary req-res secenario

def run_cmd (conn):
    BUFFER_SIZE = 1024
    print ("Properties of the connection {}".format(conn))
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print ("Recieved data: {}\n".format(data))
        print ("Running recvd data as commands.")
        proc = subprocess.Popen(data, shell=True, stderr=subprocess.PIPE,
                                                     stdout=subprocess.PIPE)
        if proc:
            output=(proc.stdout.read())
            print ("Output:",output)
            conn.sendall(output)

        else:
            error=(proc.stderr.read())
            print ("Error:",error)
            conn.sendall(error)
        # was yield
        return data


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
        print ("raw bites recvd ", req_raw)
        req_decoded = req_raw.decode('utf-8')
        print (req_decoded)
        if req_decoded == "exit":
            break
        res_raw = res(req_decoded)
        print ("from res() function ",res_raw)
        res_encoded = res_raw.encode('utf-8')
        client_connection.sendall(res_encoded)
    client_connection.close()
    return

def listen_server():
    HOST = '127.0.01' # localhost
    PORT = 9999 # some port
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
if __name__ == '__main__':
    listen_server()
