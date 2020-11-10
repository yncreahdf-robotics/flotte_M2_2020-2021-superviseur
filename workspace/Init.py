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

my_ip=IPFinder.get_my_ip()
port = 1883

hosts = open('/etc/hosts','r')
for line in hosts:
	try:
		if line.split()[1] == "supIP":
			ipsuperviseur = line.split()[0]
	except IndexError:
		pass

type_robot="Turlebot"

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
	if (msg.topic=="Initialisation/Feedback" and msg.payload.decode("utf-8").split("/")[0]==my_ip):
		global ipsuperviseur
		ipsuperviseur=msg.payload.decode("utf-8").split("/")[1]
		print(ipsuperviseur)
		publish(ipsuperviseur, 1883, "Initialisation/Type", my_ip+"/"+type_robot , 2)
		client.unsubscribe("Initialisation/+")


#Appel d'une fonction qui permet de recevoir un message

def subscribe(ip, port, topic, qos):

	global client
	client = mqtt.Client()

	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.connect(ip,port,60)
	client.subscribe(topic, qos)
	client.loop_start()


#Appel d'une fonction qui permet d'envoyer un message

def publish(ip, port, topic, message, qos):

	client2 = mqtt.Client()

	client2.connect(ip,port,60)
	client2.loop_start()
	client2.publish(topic, message, qos)
	print("message envoye sur "+topic)


###################################
###	PROGRAMME PRINCIPAL	###
###################################


i=0

#	Send the robot's IP to all connected ip

publish(ipsuperviseur, 1883, "Initialisation/Envoi", my_ip , 2)

while(1):
	i+=1
	print(i)
	time.sleep(10)






