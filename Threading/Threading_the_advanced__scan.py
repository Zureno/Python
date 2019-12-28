import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)
def connScan(tgtHost,tgtPort):


