#!/bin/python

########################################
#                                      #
#         TCP Excerises - HTTP         #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: Cryptid                      #
# Created: 05/05/2020                  #
# Version: v0.5                        #
#                                      #
########################################

import socket
import sys

buffer_size = 1024

def MakeHTTPRequest(target):
    if target['path'] == '':
        target['path'] = '/'
    request =  f"GET {target['path']} HTTP/1.0 \r\n"
    #request = "GET / HTTP/1.0 \r\n"
    request += "\r\n"
    print(request)
    #.encode('utf-8')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target['host'], 80))
    s.sendall(request.encode('utf-8'))
    data = s.recv(buffer_size)
    s.close()
    return data

def ParseUrl(target):
    split_target = target.split("://", maxsplit=1)

    protocol = split_target[0]
    url      = split_target[1]
    
    if '/' in url:
        url_host = url.split("/", maxsplit=1)[0]
        url_path = url.split("/", maxsplit=1)[1]
    else:
        url_host = url.split("/", maxsplit=1)[0]
        url_path = ""
    return {'protocol': protocol, 'host': url_host, 'path': url_path}

def main():
    target = sys.argv[1]
    #target = "http://google.com/"
    print(MakeHTTPRequest(ParseUrl(target)))

if __name__ == "__main__":
    main()

