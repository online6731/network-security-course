from api import app
from sniffer import Sniffer


server_socket_ip = '0.0.0.0'
server_socket_port = 5000
sniffing_interface = 'enp3s0'

if __name__ == '__main__':
    Sniffer().run(interface=sniffing_interface)
    socketio.run(app)
