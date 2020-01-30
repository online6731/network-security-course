from api import app
from sniffer import Sniffer

server_socket_ip = '0.0.0.0'
server_socket_port = 12345
sniffing_interface = 'enp3s0'

if __name__ == '__main__':
    Sniffer().run(socket_address=(server_socket_ip, server_socket_port), interface=sniffing_interface)
    app.run(debug=True, host='0.0.0.0')
