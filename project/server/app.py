from api import run_sniffer, app, socketio

if __name__ == '__main__':
    run_sniffer()
    socketio.run(app)
