from flask_socketio import emit
from kamene.all import *
import json
import scapy2dict
import threading
import os
from socket_api import socketio
# from kamene.config import conf
# conf.ipv6_enabled = False


class Sniffer:
    """
    This class is responsible for sniffing and analysing packets.
    It also sends this information over socket to clients.
    """

    def __init__(self, interface):
        # self.sock = sock
        self.interface = interface

    def process_packets(self, packet):
        """process and analyse receiving packet and send the result over socket to all clients"""

        packet = dict(scapy2dict.to_dict(packet))

        # TODO : fix the try-except statements
        try:
            del packet['IP']['options']
        except:
            pass

        try:
            del packet['TCP']['options']
        except:
            pass

        from random import randint
        if randint(1, 100) == 100:
            print(packet)
            socketio.emit('new_packet', " {'packet': packet}", broadcast=True)
            socketio.send(" {'packet': packet}", broadcast=True)

    def run(self):
        """start the packet sniffing process"""

        sniff(iface=self.interface, store=False, prn=self.process_packets)
