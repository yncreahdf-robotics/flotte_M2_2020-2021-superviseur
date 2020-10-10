#!/usr/bin/env python

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


if __name__ == '__main__':


	client = mqtt.Client()
	client.connect("192.168.1.4",1883,60)
	client.on_connect = on_connect

	while True:
 		client.on_disconnect = on_disconnect
		client.publish("topic/donneesRobots", "50% de batterie", qos=0)
		time.sleep(5)

