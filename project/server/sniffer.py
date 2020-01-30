import scapy.all as scapy
import argparse
import os
import socketserver
import threading


client_sockets = [] #TODO : use proper shared memory methods instead of global vars

class Sniffer():
    server_socket_ip = ''
    server_socket_port = 12345
    server_socket_address = (server_socket_ip, server_socket_port)

    @staticmethod
    def get_socket_connections(server_socket):
        """keeps receiving socket connections"""

        global client_sockets

        while True:
            client_socket, client_socket_address = server_socket.accept()
            client_sockets.append(client_socket)


    def start_server_socket(self):
        """starts the socket server"""

        server_socket = socket.socket()
        server_socket.bind(self.server_socket_address)
        server_socket.listen()
        threading.Thread(target=self.get_socket_connections, args=(server_socket, )).start()


    def process_packets(self, packet):
        """process and analyse receiving packet and send the result over socket to all clients"""

        global client_sockets

        for client_socket in client_sockets:
            try:
                client_socket.send(str(packet.mysummary).encode())
            except:
                pass


    def start_sniffing(self):
        """start the packet sniffing process"""

        scapy.sniff(iface='wlp2s0', store=False, prn=self.process_packets)

    def run(self):
        self.start_server_socket()
        self.start_sniffing()