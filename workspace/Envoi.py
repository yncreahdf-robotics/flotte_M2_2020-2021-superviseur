
#!/usr/bin/env python

import paho.mqtt.client as mqtt
import time

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



#Appel d'une fonction qui permet de recevoir un message

def subscribe(ip, port, topic, qos):

	client = mqtt.Client()

	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.connect(ip,port,60)
	client.subscribe(topic, qos)
	client.loop_start()


#Appel d'une fonction qui permet d'envoyer un message

def publish(ip, port, topic, message, qos):

	client = mqtt.Client()

	client.connect(ip,port,60)
	client.loop_start()
	client.publish(topic, message, qos)

publish(ip, 1883, "topiCoco", "testmessage", 2)


while (1):
	time.sleep(5)
	print("ok")
