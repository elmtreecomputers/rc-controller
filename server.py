from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(j):
    print('received json: ' + str(j))
#    j = json.loads(str(j))
    try:
        print(j["x"] ," and ", j["y"])
    except:
        print("")
# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():  
    message = "Hello, World"
    return render_template('client.html', message=message)
    
if __name__ == '__main__':
    socketio.run(app)
   # app.run(debug=True)
