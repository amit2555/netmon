#!/usr/bin/env python

#--------------------------------------------------------
# This is a simple UDP Pinger that sends UDP Pings using
# different Source Ports, calculates latency and monitors
# packet loss.
#--------------------------------------------------------

from socket import *
from datetime import datetime
from kafka import KafkaProducer
import time
import json


def main():
    server_name = "localhost"
    message = "ping"
    i = 0
    d = dict()

    producer = KafkaProducer(bootstrap_servers="localhost:9092",
                             key_serializer = str.encode,
                             value_serializer=lambda x:json.dumps(x).encode('utf-8'))
    while i < 5:
        client_socket = socket(AF_INET, SOCK_DGRAM)
        sport = 65000
        dport = 12000
        client_socket.bind(('', sport))
        start_time = datetime.now()
        client_socket.sendto(message, (server_name, dport))
        client_socket.settimeout(5)
        try:
            message, server_address = client_socket.recvfrom(1024)
            end_time = datetime.now()
            rtt = end_time - start_time
            d = {'rtt': rtt.microseconds}
        except timeout:
            continue
        i += 1
        producer.send('netmon',key='kafka_key',value='{}\t{}\t{}'.format(server_name,sport,rtt.microseconds))

        time.sleep(1)
    client_socket.close()

if __name__ == "__main__":
    main()


