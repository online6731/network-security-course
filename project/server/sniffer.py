import scapy.all as scapy
import argparse
import os
import socketserver
import threading
import scapy2dict
import json


client_sockets = [] #TODO : use proper shared memory methods instead of global vars

class Sniffer():
    """
    This class is responsible for sniffing and analysing packets.
    It also sends this information over socket to clients.
    """

    @staticmethod
    def get_socket_connections(server_socket):
        """keeps receiving socket connections"""

        global client_sockets

        while True:
            client_socket, client_socket_address = server_socket.accept()
            client_sockets.append(client_socket)


    def start_server_socket(self, socket_address):
        """starts the socket server"""

        server_socket = socket.socket()
        server_socket.bind(socket_address)
        server_socket.listen()
        threading.Thread(target=self.get_socket_connections, args=(server_socket, )).start()


    def process_packets(self, packet):
        """process and analyse receiving packet and send the result over socket to all clients"""

        global client_sockets

        packet = dict(scapy2dict.to_dict(packet))

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

        scapy.sniff(iface=interface, store=False, prn=self.process_packets)


    def run(self, socket_address, interface):
        self.start_server_socket(socket_address=socket_address)
        self.start_sniffing(interface=interface)