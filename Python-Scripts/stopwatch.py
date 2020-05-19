#!/bin/python

########################################
#                                      #
#         Stop watch Script            #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: Cryptid Khaos                #
# Created: 19/05/2020                  #
# Last update: 19/5/2020                #
# Version: v1.0                        #
#                                      #
########################################

import time
import sys


# User Introduction
def intro():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("     Stop watch - {:s}".format(sys.argv[1]))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


class Stopwatch:
    def __init__(self):
        self.start_TimeStamp = self.__Timestamp()

    def __Timestamp(self):
        return time.perf_counter()

    def __ElapsedSecs(self):
        return self.__Timestamp() - self.start_TimeStamp

    def FormmatedElapsed(self):
        return time.strftime('%H:%M:%S  ',
                             time.gmtime(self.__ElapsedSecs()))


def loop(swatch):
    while(True):
        print(swatch.FormmatedElapsed(), end='\r')
        time.sleep(0.1)


# Main function
def main():
    if len(sys.argv) == 1:
        sys.argv.append("")
    intro()
    loop(Stopwatch())


if __name__ == "__main__":
    main()
