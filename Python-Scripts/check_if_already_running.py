# Test code snippet from stackoverflow
# https://stackoverflow.com/questions/788411/check-to-see-if-python-script-is-running

import psutil
import os

#Tested to run on Mac OS
def is_running(script):
    for q in psutil.process_iter():
        if q.name().startswith('Python'):
            if len(q.cmdline())>1 and script in q.cmdline()[1] and q.pid !=os.getpid():
                print("'{}' Process is already running".format(script))
                return True

    return False


if not is_running("check_if_already_running.py"):
    n = input("What is Your Name? ")
    print ("Hello " + n)
