
#!/usr/bin/env python

import paho.mqtt.client as mqtt
import time

client = mqtt.Client()

ip = "192.168.1.5"

def on_connect(client, userdata, flags, rc):

	print("Connected with result code "+str(rc))
	if rc==0:
		print("connection ok")
		#pass
	else:
		print("connection no")
		#pass

	


def on_disconnect(client, userdata, rc):

	print("Client Got Disconnected")


def on_message(client, userdata, msg):

	print("Yes! i receive the message :" , str(msg.payload))
	print("message received ", msg.payload.decode("utf-8"))
	print("message topic=",msg.topic)
	print("message qos=",msg.qos)
	print("message retain flag=",msg.retain)

	if msg.topic == "Initialisation/Envoi":

		global menu_accueil

		if not msg.payload.decode("utf-8") in menu_accueil:

			menu_accueil.append(msg.payload.decode("utf-8"))

		AvailableIP = IPFinder.launch

		for ip in AvailableIP():

			try:
				publish(ip, port, "Initialisation/Feedback", msg.payload.decode("utf-8") + "/" + my_ip, 2)

			except OSError as err:

				pass

	if msg.topic == "Initialisation/Type":

		print("c'est bon le type est : " + msg.payload.decode("utf-8"))



client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect(ip,1883,60)
client.subscribe("topiCoco", 2)
client.loop_start()

i = 0

while i < 5:
	time.sleep(1)
	print(i)
	i = i + 1

client.unsubscribe("topiCoco")

while 1:
	time.sleep(1)
	print("ok")
