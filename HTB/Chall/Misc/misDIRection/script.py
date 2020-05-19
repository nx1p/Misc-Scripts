#!/bin/python

########################################
#                                      #
#         misDIRection Script          #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: Marceline Kuo-Arrigo         #
# Created: 13/12/2019                  #
# Last update: 19/5/2020                #
# Version: v1.2                        #
#                                      #
########################################
# #### Challange Description
#  During an assessment of a unix system the HTB team found
#  a suspicious directory.
#  They looked at everything within but couldn't find any files
#  with malicious intent.
#
# #### Script Description
# This script will go through a list of directories some with files in them
# and sort them by the number of the file in the directory.
# Ignoring directories without files.
#
# For example X directory could have a file in it labeled 4
# and a Y directory could have a file in it labeled 3
# So Y will go before X #
# So by doing this the script will put together
# what I hope is the flag for the challenge.
#

import subprocess
import base64


# User Introduction
def intro():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("     misDIRection Script")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")


# Provides a dict of files
class DIRDict:
    def __runFind(self):
        return subprocess.run("find .secret -type f | sed 's!.secret/!!'",
                              shell=True,
                              check=True,
                              universal_newlines=True,
                              stdout=subprocess.PIPE).stdout

    def __SplitByLine(self):
        return self.__runFind().splitlines()

    def __splitEach(self, line):
        splitted = line.split('/')
        splitted.reverse()
        return splitted

    def __splitAllIntoKeyPair(self):
        return map(self.__splitEach, self.__SplitByLine())

    def __convertToDict(self):
        return dict(self.__splitAllIntoKeyPair())

    def __getDIRDict(self):
        return self.__convertToDict()

    def __init__(self):
        self.dict = self.__getDIRDict()


def ConvertToString(dirdict, flag=''):
    if len(flag) != len(dirdict):
        flag += dirdict[str(len(flag)+1)]
        return ConvertToString(dirdict, flag=flag)
    elif len(flag) == len(dirdict):
        return flag


def Log(msg):
    print("   > "+msg)


# Main function
def main():
    intro()
    dirdict = DIRDict().dict
    EncodedFlag = ConvertToString(dirdict)
    DecodedFlag = base64.b64decode(EncodedFlag)
    Log("Encoded Flag: "+EncodedFlag)
    Log("Decoded Flag: "+str(DecodedFlag))


if __name__ == "__main__":
    main()
