#!/usr/bin/env python

#------------------------------------------------------------
# This is a multi-threaded UDP Ponger script that echo's message
# received on listening port.
#------------------------------------------------------------


import SocketServer


SERVER_HOST = 'localhost'
SERVER_PORT = 12000


class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        """Send echo back to Client."""
        data, socket = self.request
        socket.sendto(data, self.client_address)
        return None


class ForkingServer(SocketServer.ForkingMixIn, SocketServer.UDPServer):
    pass


def main():
    # Start a server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), 
                           ForkingServerRequestHandler)

    server.serve_forever()


if __name__ == "__main__":
    main()

