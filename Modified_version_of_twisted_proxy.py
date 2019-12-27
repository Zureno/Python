#!/usr/bin/python

import socket
import sys
import getopt
import os
import datetime
import time
from twisted.internet import protocol,reactor
from twisted.protocols import basic
from twisted.python import log

class bcolors:
    HEADER = '\080[95m'
    OKBLUE = '\034[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():   
    print bcolors.HEADER + "   ________                    ____  ______  _____             __                               " + bcolors.ENDC
    print bcolors.HEADER + "  /________/  _        _  _   / ___// ____/ / ___/ _ __       / __ \ ___  __  _    _ _    _     " + bcolors.ENDC
    print bcolors.HEADER + "     / /\ \  / /\ \  / / / / /_/__   / /   /  _ //  _  \     / /_/ //__ / _ \ \ \_/ /\_\ / /    " + bcolors.ENDC
    print bcolors.HEADER + "    / /  \ \/ /  \ \/ / / / ___/ /  / /   / /__ / /_ / /    / /  / / / | |_| | \   /    / /     " + bcolors.ENDC
    print bcolors.HEADER + "   /_/    \_\/    \_\/ /_/ /__/_/  /_/   /____//_ ___ /    /_/    /_/   \ _ / /_/ \_\  /_/      " + bcolors.ENDC
    print
    print bcolors.HEADER + "                             Created By: Pranshu Raghav                                         " + bcolors.ENDC
    print bcolors.HEADER + "                                                                                                " + bcolors.ENDC


def usage():
    print "Twisted Proxy :- A Simple Python based proxy based on twisted module. "
    print "----------------------------------------------------------------------------"

class ServerProtocol(protocol.Protocol): 
    
    def __init__(self):
        self.buffer = None
        self.client = None
        def connectionMade(self):
        factory = protocol.ClientFactory()
        factory.protocol = ClientProtocol
        factory.server = self

        reactor.connectTCP('<IP-address>','<Port Number>',factory)

    def dataReceived(self, data):
        if (self.client!= None):
            self.client.write(data)
        else:
            self.buffer = data

    def write(self, data):
        self.transport.write(data)

        print 'Server:' + data.encode('hex')

class ClientProtocol(protocol.Protocol):
    
    def connectionMade(self):
        self.factory.server.client = self
        self.write(self.factory.server.buffer)
        self.factory.server.buffer = ''

    def dataReceived(self,data):
        self.factory.server.write(data)
    
    def write(self,data):
        self.transport.write(data)
        print 'Client:' + data.encode('hex')

def main():
    
    banner()
    usage()

    log.startLogging(sys.stdout)
    factory = protocol.ServerFactory()
    factory.protocol = ServerProtocol
    reactor.listenTCP(2222,factory)
    reactor.run()

if __name__== '__main__':
    main()

