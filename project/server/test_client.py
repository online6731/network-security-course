import socketio

sio = socketio.Client()
sio.connect('http://localhost:12345')

@sio.on('new_packet', namespace='/packet')
def on_new_packet():
    print("I'm connected to the /chat namespace!")
