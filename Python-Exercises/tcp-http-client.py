#!/bin/python

########################################
#                                      #
#         TCP Excerises - HTTP         #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: Cryptid                      #
# Created: 05/05/2020                  #
# Version: v0.1                        #
#                                      #
########################################

import socket
import sys

port = 80
buffer_size = 1024

def MakeHTTPRequest(url):
    request = "GET / HTTP/1.0 \r\n"
    request += "\n"
    #.encode('utf-8')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendall(MESSAGE)
    data = s.recv(buffer_size)
    s.close()

def PraseUrl(target):
    protocol = target.split("://", maxsplit=1)[0]
    url = target.split("://", maxsplit=1)[1]
    return url


def main():
    #target = sys.argv[1]
    target = "http://google.com/"
    MakeHTTPRequest(target)
    print("received data:", data)

if __name__ == "__main__":
    main()

