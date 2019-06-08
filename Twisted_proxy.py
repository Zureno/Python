from twisted.internet import protocol, reactor
from twisted.protocols import basic

class proxy_ServerProtocol(protocol.Protocol):
    def __init__(self):
        self.buffer = None
        self.client = None

    def connectionMade(self):
        factory = protocol.ClientFactory()
        factory.protocol = proxy_ClientProtocol
        factory.server = self

        reactor.connectTCP('ec2-54-89-126-237.compute-1.amazonaws.com',6675, factory)

    def dataReceived(self, data):
        if (self.client != None):
            self.client.write(data)
        else:
            self.buffer = data

    def write(self, data):
        self.transport.write(data)
        print 'Server: ' + data.encode('hex')

class proxy_ClientProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.server.client = self
        self.write(self.factory.server.buffer)
        self.factory.server.buffer = ''

    def dataReceived(self, data):
        self.factory.server.write(data)

    def write(self, data):
        self.transport.write(data)
        print 'Client: ' + data.encode('hex')

def main():
    import sys
    from twisted.python import log

    log.startLogging(sys.stdout)

    factory = protocol.ServerFactory()
    factory.protocol = proxy_ServerProtocol

    reactor.listenTCP(6666, factory)
    reactor.run()

if __name__ == '__main__':
    main()
