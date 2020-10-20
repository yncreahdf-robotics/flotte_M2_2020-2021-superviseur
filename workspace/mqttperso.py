#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time


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


def subscribe(ip, port, topic, qos):

	client = mqtt.Client()

	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect

	

	client.connect(ip,port,60)

	client.subscribe(topic, qos)

	client.loop_start()

	


def publish(ip, port, topic, message, qos):

	client = mqtt.Client()

	client.connect(ip,port,60)

	

	client.loop_start()

	

	client.publish(topic, message, qos)







