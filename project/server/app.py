from api import app
from sniffer import Sniffer
import argparse


server_socket_ip = '0.0.0.0'
server_socket_port = 5000
sniffing_interface = 'enp3s0'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--interface')
    args = parser.parse_args()
    sniffing_interface = args.interface if args.interface else sniffing_interface

    Sniffer().run(interface=sniffing_interface)
    socketio.run(app)
