#!/usr/bin/env python


#------------------------------------------------------------
# This is a simple UDP Ponger script that echo's message
# received on listening port.
#------------------------------------------------------------

from socket import *


def main():
    # Open a UDP socket and bind to a port
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', 12000))

    # Receive message from Clients and echo back
    while True:
        message, address = server_socket.recvfrom(1024)
        print message, address
        server_socket.sendto(message, address)


if __name__ == "__main__":
    main()

