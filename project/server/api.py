from flask import Flask
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# TODO : add parameter validation to api

@app.route('/interfaces')
def interfaces():
    """sends a list all available interfaces"""

    return '''{
        data: []
    }'''


@app.route('/analyse')
def analyse():
    """analyse a pcap file and returns the result"""


    pcap_file = request.files["pcap_file"]

    return {
        data: {}
    }

def send_packet(packet):
    emit('new_packet', {'packet': packet})
