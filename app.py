from flask import Flask, render_template
from flask_socketio import SocketIO
import rtmidi
import threading

app = Flask(__name__)
socketio = SocketIO(app)

NUM_OF_NOTES = 100
note_history = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connected')
def handle_connect():
    print('client has connected.')
    
def midi_input_handler():
    midiin = rtmidi.RtMidiIn()
    ports = range(midiin.getPortCount())
    if ports:
        for i in ports:
            print(midiin.getPortName(i))
        midiin.openPort(len(ports) - 1)
        while True:
            m = midiin.getMessage(250)  # some timeout in ms
            if m:
                if m.isNoteOn():
                    note_data = m.getMidiNoteName(m.getNoteNumber())
                    note_name = note_data[0]
                    note_location = note_data[1:]
                    note_history.append(note_name)
                    print(note_history)
                    if len(note_history) > NUM_OF_NOTES:    # Starts to remove older notes once list gets too large
                        note_history.pop(0)
                    velocity = m.getVelocity()
                    print('ON: ', note_name, velocity, note_location)
                    socketio.emit('onNotePlayed', {'note': note_name, 'velocity': velocity, 'location': note_location})
    else:
        print('NO MIDI INPUT PORTS!')
    
if __name__ == '__main__':
    midi_thread = threading.Thread(target=midi_input_handler)
    # Daemonize the thread so it automatically dies when the main thread ends
    midi_thread.daemon = True
    midi_thread.start()

    socketio.run(app, host='0.0.0.0', debug=True, port=5001)