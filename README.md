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



## Docker 


build


```
docker build -t postputprinter .
```

then run

```
docker run -d --rm --hostname postputprinter --name postputprinter -p 8051:8051 postputprinter
```

and then test it

```
docker run --rm   -it curlimages/curl:8.9.1  -v -s -S -X POST http://postputprinter:8051     --header 'Content-Type: application/json; charset=utf-8'     --header 'Accept: application/json'     --header 'User-Agent: orion/0.10.0'   --header  "Fiware-Service: demo"     --header "Fiware-ServicePath: /test"     -d  '{
         "data": [
             {
                 "id": "R1","type": "Node",
                 "co": {"type": "Float","value": 0,"metadata": {}},
                 "co2": {"type": "Float","value": 0,"metadata": {}},
                 "humidity": {"type": "Float","value": 40,"metadata": {}},
                 "pressure": {"type": "Float","value": 1.0,"metadata": {}},
                 "temperature": {"type": "Float","value": 1.0,"metadata": {}},
                 "wind_speed": {"type": "Float","value": 1.06,"metadata": {}}
             }
         ],
         "subscriptionId": "57458eb60962ef754e7c0998"
     }'

```