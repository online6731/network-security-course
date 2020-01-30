from flask import Flask

app = Flask(__name__)

@app.route('/interfaces')
def interfaces():
    """sends a list all available interfaces"""

    return {
        data: []
        }

@app.route('/analyse_pcap')
def analyse_pcap():
    """analyse a pcap file and returns the result"""

    return {
        data: {}
    }
