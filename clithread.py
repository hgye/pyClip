#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
import socket
import select

class ClipThread(Thread):
    """
    This is cli thread.
    which will maintenance the TCP connection with board cliproxy
    """
    def __init__(self, server_ip, server_port):
        Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = server_ip
        self.server_port = server_port

    def start(self):
        """
        start a socket connection with cliproxy
        """
        sock.connect((server_ip, server_port))

    def run(self):
        """
        """
        clist = command()
        for cl in clist:
        
            

