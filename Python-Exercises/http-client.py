#!/bin/python

########################################
#                                      #
#         TCP Excerises - HTTP         #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: Cryptid                      #
# Created: 05/05/2020                  #
# Version: v0.6                        #
#                                      #
########################################

import socket
import sys

buffer_size = 1024

# Composes HTTP request using parsed infomation
# And then makes the request using TCP sockets
# Example input:
#  {'protocol': 'http', 'host': 'google.com', 'path': ''}
def MakeHTTPRequest(target):
    if target['path'] == '':
        target['path'] = '/'
    request =  f"GET {target['path']} HTTP/1.0 \r\n"
    request += "\r\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target['host'], 80))
    s.sendall(request.encode('utf-8'))
    data = s.recv(buffer_size)
    s.close()
    return data

#Parses a target url (e.g. "http://google.com/") into protocol, host and path.
# Example Input:
#  "http://google.com"
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

#Main function, linear list of instructions, calls other functions and ties everything together
def main():
    target = sys.argv[1]
    #target = "http://google.com/"
    print(MakeHTTPRequest(ParseUrl(target)))

if __name__ == "__main__":
    main()

