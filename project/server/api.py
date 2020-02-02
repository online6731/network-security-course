from flask import Flask

app = Flask(__name__)

# TODO : add parameter validation to api

@app.route('/interfaces')
def interfaces():
    """sends a list all available interfaces"""

    return {
        data: []
    }


@app.route('/analyse')
def analyse():
    """analyse a pcap file and returns the result"""


    pcap_file = request.files["pcap_file"]

    return {
        data: {}
    }
