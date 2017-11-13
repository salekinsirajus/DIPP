import unittest
from client import initSocket, connectNode, sendMessage
import socket

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class clientTest(unittest.TestCase):
        # add contex to these raises
    def test_garbage_string(self):
        self.assertRaises(ValueError, initSocket("bleh"))
    def test_intger_input(self): 
        self.assertRaises(ValueError, initSocket(0))
    def test_misleading_input(self):
        self.assertRaises(ValueError, initSocket("datagram"))
    # find a better way to test the sockets
    # They need to be closed after initializing
    def test_socket_input(self):
        self.assertIsInstance(initSocket('SOCK_DGRAM'), type(udp_sock))
    def test_send_sample_msg(self):
        sock = initSocket('SOCK_STREAM')
        sock = connectNode(sock, '127.0.0.1', 9999)
        self.assertEqual(sendMessage(sock, "some msg"), 0)
            

if __name__ == '__main__':
    unittest.main()
