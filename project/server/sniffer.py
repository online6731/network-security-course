from kamene.all import *
import argparse
import os
import socketserver
import threading
import scapy2dict
import json
from api import send_packet

client_sockets = [] #TODO : use proper shared memory methods instead of global vars

class Sniffer():
    """
    This class is responsible for sniffing and analysing packets.
    It also sends this information over socket to clients.
    """

    def process_packets(self, packet):
        """process and analyse receiving packet and send the result over socket to all clients"""

        global client_sockets

        packet = dict(scapy2dict.to_dict(packet))


        # TODO : fix the try-except statements
        try:
            del packet['IP']['options']
        except: pass

        try:
            del packet['TCP']['options']
        except: pass

        for client_socket in client_sockets:
            try:
                client_socket.send(json.dumps(packet))
            except: pass

        # print(packet)

    def start_sniffing(self, interface):
        """start the packet sniffing process"""

        sniff(iface=interface, store=False, prn=self.process_packets)


    def run(self, interface):
        self.start_sniffing(interface=interface)