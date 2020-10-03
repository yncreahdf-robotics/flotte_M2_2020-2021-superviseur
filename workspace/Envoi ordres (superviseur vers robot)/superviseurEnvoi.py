#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
# This is the Publisher


def on_connect(client, userdata, flags, rc):

	print("Connected with result code "+str(rc))
	if rc==0:
		print("ok")
	else:
		print("no")


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
	client.connect("192.168.1.4",1883,60)
	client.on_connect = on_connect
	client.on_message = on_message
 	client.on_disconnect = on_disconnect
	
	client.publish("topic/OrdreRobot", "1", qos=2)

