# -*- coding: utf-8 -*-

############################################################
### Programme principal à lancer pour démarrer le projet ###
############################################################


###############
### Imports ###
###############

# Import des fichiers .py propre au projet

#import FonctionsMQTT

import IPFinder
import paho.mqtt.client as mqtt

# Import des librairies exterieures au projet

import time


##########################
### Variables globales ###
##########################

port = 1883
ipsuperviseur=""


######################
### Initialisation ###
######################


############
### Defs ###
############

#!/usr/bin/env python3

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
	print("message received ", msg.payload.decode("utf-8"))
        #with open('data.json', 'w') as f:
        #json.dumps(msg.payload.decode("utf-8"))
	print("message topic=",msg.topic)
	print("message qos=",msg.qos)
	print("message retain flag=",msg.retain)
	if (msg.topic=="Initialisation/Feedback"):	
		global ipsuperviseur
		ipsuperviseur=msg.payload.decode("utf-8")


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


###################################
###	PROGRAMME PRINCIPAL	###
###################################

#	subscribe to the Feedback topic
subscribe(IPFinder.get_my_ip(),1883, "Initialisation/Feedback",2)

#	Send the robot's IP to all connected ip
AvailableIP=IPFinder.launch
for ip in AvailableIP():
	try:
		publish(ip, 1883, "Initialisation/Envoi", str(IPFinder.get_my_ip()) , 2)	

	except OSError as err:
		print("OS error: {0}".format(err))

while(1):
	print(ipsuperviseur)
	time.sleep(10)

		




