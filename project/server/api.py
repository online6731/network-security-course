import scapy2dict
from kamene.config import conf
conf.ipv6_enabled = False
from kamene.all import *
from flask_socketio import emit
from flask_socketio import SocketIO, emit, send
from flask import Flask
from flask import Flask, send_from_directory
from threading import Thread
import os
import argparse
import threading
import jsonpickle
import socket
from engineio.payload import Payload
from functools import partial
from config import last_packet, default_interface


app = Flask(__name__)
app.config['SECRET_KEY'] = 'xi65056ux5n0hdXn878918797*/-*18-+*'

socketio = SocketIO(app, cors_allowed_origins='*')
Payload.max_decode_packets = 50000

@app.route('/info')
def info():
    """return network information including interfaces, ..."""

    try:
        packet_list = rdpcap('example.pcap')
        packets = [dict(scapy2dict.to_dict(packet)) for packet in packet_list][:2]

        return jsonpickle.encode({
            'ok': True,
            'interfaces': [iface[1] for iface in socket.if_nameindex()]
        })

    except error as Exception:
        return jsonpickle.encode({
            'ok': False,
            'error': error
        })


@app.route('/analyse')
def analyse():
    """analyse a pcap file and returns the a list of analysed packets"""

    # pcap_file = request.files["pcap_file"]

    try:
        packet_list = rdpcap('example.pcap')
        packets = [dict(scapy2dict.to_dict(packet)) for packet in packet_list][:2]

        return jsonpickle.encode({
            'ok': True,
            'data': packets
        })

    except error as Exception:
        return jsonpickle.encode({
            'ok': False,
            'error': error
        })


@app.route('/favicon.ico')
def favicon():
    """return the favicon or logo of app"""

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@socketio.on('client_state')
def client_state(msg):
    try:
        if globals()['last_packet'] != None and msg == 'ready':
            emit('new_packet', jsonpickle.encode(globals()['last_packet']), broadcast=True)
            globals()['last_packet'] = None
    except:
        pass


def process_packets(packet):
        """process and analyse receiving packet and stores the result"""

        globals()['last_packet'] = dict(scapy2dict.to_dict(packet))

        # socketio.emit('new_packet', " {'packet': packet}", broadcast=True)
        # socketio.send(" {'packet': packet}", broadcast=True)


def run_sniffer(interface=None):
    """starts the sniffer"""

    interface = interface if interface != None else default_interface

    print(f'Starting the sniffing process on {interface} ...')
    sniffer = partial(sniff, iface=interface, store=False, prn=process_packets)
    threading.Thread(target=sniffer).start()