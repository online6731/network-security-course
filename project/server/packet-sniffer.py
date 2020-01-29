import scapy.all as scapy
import argparse
import os
import socket
import threading


server_socket_ip = ''
server_socket_port = 12345
server_socket_address = (server_socket_ip, server_socket_port)

client_sockets = []


def get_socket_connections(server_socket):
    """keeps receiving socket connections"""

    global client_sockets

    while True:
        client_socket, client_socket_address = server_socket.accept()
        client_sockets.append(client_socket)


def start_server_socket(server_socket_address):
    """starts the socket server"""

    server_socket = socket.socket()
    server_socket.bind(server_socket_address)
    server_socket.listen()
    threading.Thread(target=get_socket_connections, args=(server_socket, )).start()
    print('start_server_socket started')


def process_packets(packet):
    """process and analyse receiving packet and send the result over socket to all clients"""

    global client_sockets

    for client_socket in client_sockets:
        try:
            client_socket.send(str(packet.mysummary).encode())
        except:
            pass


def start_sniffing():
    """start the packet sniffing process"""

    scapy.sniff(iface='wlp2s0', store=False, prn=process_packets)


if __name__ == '__main__':
    start_server_socket(server_socket_address)
    start_sniffing()