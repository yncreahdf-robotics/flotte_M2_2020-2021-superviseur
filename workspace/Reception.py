
#!/usr/bin/env python

import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

# Callbacks

def on_connect(client, userdata, flags, rc):

	print("Connected with result code "+str(rc))
	if rc==0:
		print("ok")
	else:
		print("no")
	#client.subscribe("topic/DonneesRobots", qos=0)
	client.subscribe("topic/TopiCoco", qos=1)

def on_disconnect(client, userdata, rc):

	print("Client Got Disconnected")

def on_message(client, userdata, msg):

	print("Yes! i receive the message :" , str(msg.payload))
	print("message received " ,str(msg.payload.decode("utf-8")))
	print("message topic=",msg.topic)
	print("message qos=",msg.qos)
	print("message retain flag=",msg.retain)


if __name__ == '__main__':


	client = mqtt.Client()	
	client.connect("192.168.1.3",1883,60)
	client.on_connect = on_connect
	client.on_message = on_message
 	client.on_disconnect = on_disconnect

	client.loop_forever()

	while (1):
		print("ok")
