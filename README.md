# postputprinter
This is a little example to print the post and read request received by Flask web server.
The flask web server, using *socketio*, send the string of json request data to *ReactJS* frontend, which visualize in realtime.

## Usage

In a terminal 

```
python3 postputprinter.py
```
Then open browser and go to `http://localhost:5000/web`.

In another terminal
```
 curl -XPOST -d '{"id": 121,"text": 18}' -H "Content-Type: application/json" http://localhost:5000/
```
Then you see the received JSON.
