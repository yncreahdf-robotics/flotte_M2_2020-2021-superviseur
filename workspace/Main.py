# -*- coding: utf-8 -*-

############################################################
### Programme principal à lancer pour démarrer le projet ###
############################################################




###############
### Imports ###
###############


# Import des fichiers .py propre au projet

import IHM
import IPFinder
import InitBDDSuperviseur
import Robot
import Positions
import Type


# Import des librairies exterieures au projet

import curses
import time
import threading
import paho.mqtt.client as mqtt
import mysql.connector
import datetime



##########################
### Variables globales ###
##########################

#	gets the supervisor's IP using the host file
hosts = open('/etc/hosts','r')
for line in hosts:
	splitted_line=line.split()
	try:
		if splitted_line[1]=="supIP":
			my_ip = splitted_line[0]
	except IndexError:
		pass


# TCP port used for MQTT
port = 1883


iprobot = ""



############
### Defs ###
############


def on_connect(client, userdata, flags, rc):

	print("MQTT:     Connected with result code "+str(rc))
	if rc==0:
		print("MQTT:     connection ok")
		#pass
	else:
		print("MQTT:     connection no")
		#pass

	


def on_disconnect(client, userdata, rc):

	print("Client Got Disconnected")


def on_message(client, userdata, msg):

	#print("Yes! i receive the message :" , str(msg.payload))
	#print("message received ", msg.payload.decode("utf-8"))
	#print("message topic=",msg.topic)
	#print("message qos=",msg.qos)
	#print("message retain flag=",msg.retain)


	# Topic quand un nouveau robot se connecte
	if msg.topic == "Initialisation/Envoi":

		print("MESSAGE:  Nouveau robot, mise en bdd")

		iprobot = msg.payload.decode("utf-8").split("/")[0]
		typerobot = msg.payload.decode("utf-8").split("/")[1]

		# On cherche le type de robot

		result = Type.get_Type_if_exists(mycursor, typerobot)

		# Si le type de robot n'existe pas encore on l'ajoute à la base des types

		if len(result) == 0:
#TODO: remplacer pass
			pass


		# Si le type existe on ajoute le robot à la liste des robots disponibles de la base de données

		else:
#TODO: mettre une vraie position
			Robot.insert_Robot(flotte_db, iprobot, typerobot, "0, 0, 0, 0", "Idle", datetime.datetime.now())
		

	# Topic quand une nouvelle commande arrive
	if msg.topic == "Commande/Envoi":

		print("MESSAGE:  Nouvelle commande")

		# recherche du robot dispo (+le plus proche de la destination)
					
		listeRobots=Robot.find_Robot_by_role(mycursor,"Service")

		# Vérifier que la liste n'est pas vide

		if len(listeRobots)!=0:

			# Recherche d'un preparateur disponible

			listePreparateurs = Robot.find_Robot_by_role(mycursor,"Preparateur")
	
			# Vérifier que la liste n'est pas vide

			if len(listePreparateurs)!=0:

				robotMissione = listeRobots[0]

				iprobot=robotMissione[0]

				preparateurMissione = listePreparateurs[0]

				ippreparateur=preparateurMissione[0]

				print("PUBLISH:  Envoi d'un ordre a", iprobot)

				publish(my_ip, port, "Ordre/Envoi", iprobot + "/" + "Go" + "/" + msg.payload.decode("utf-8") , 2)

				print("PUBLISH:  Envoi d'un ordre a", ippreparateur)

				publish(my_ip, port, "Ordre/Envoi", ippreparateur + "/" + "Prepare" + "/" + msg.payload.decode("utf-8") , 2)

			# Si aucun robot n'est disponible

			else:
#TODO: finir le else
				print("PUBLISH:  Aucun Préparateur Disponible")
				#	Boucler jusqu'à trouver un robot pour effectuer l'ordre


		# Si aucun robot n'est disponible

		else:
#TODO: finir le else
			print("PUBLISH:  Aucun Robot Disponible")
			#	Boucler jusqu'à trouver un robot pour effectuer l'ordre

		


	if msg.topic == "Robot/Ping":

		print("MESSAGE:  Reception d'un ping : " + msg.payload.decode("utf-8"))

		result = Robot.get_all_Robot(mycursor)
	
		for robot in result:

			Robot.update_ping(flotte_db, robot[0])
		
		



#Appel d'une fonction qui permet de recevoir un message

def subscribe(ip, port, topic, qos):

	client = mqtt.Client()

	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.connect(ip,port,60)
	client.subscribe(topic, qos)
	client.loop_start()
	print("MQTT:     subscribe to "+topic)



#Appel d'une fonction qui permet d'envoyer un message

def publish(ip, port, topic, message, qos):

	client = mqtt.Client()

	client.connect(ip,port,60)
	client.loop_start()
	client.publish(topic, message, qos)
	print("PUBLISH:  message sent to "+topic)



# Verifier que les robots en marche sont toujours en marche

def pingRobots():

	threading.Timer(30, pingRobots).start()	# Recommence toute les 20 sec

	result = Robot.get_all_Robot(mycursor)
	
	print("PING:     Ping des robots ...")

	for robot in result:

		if (datetime.datetime.now() - robot[4]) > datetime.timedelta(seconds=30):

			print("PING:     Robot ", robot[1], " (", robot[0], ") ", " deconnecte")
			Robot.delete_Robot(flotte_db, robot[0])

		else:
			print("PING:     Robot ", robot[1], " (", robot[0], ") ", " ok")


	print("PING:     Ping terminé")
		



######################
### Initialisation ###
######################


# Lancement IHM Initialisation


###	CONNECTS TO DATABASE	### 
flotte_db=mysql.connector.connect(
	host='localhost',
	user='root',
	password='L@boRobotique'
)

global mycursor
mycursor=flotte_db.cursor()

InitBDDSuperviseur.delete_flotte_db(flotte_db)

InitBDDSuperviseur.create_flotte_db(flotte_db)

InitBDDSuperviseur.create_all_tables(flotte_db)

Positions.insert_Pose(flotte_db, "recharge", 0.2, 4.4, -0.1, -1)
Positions.insert_Pose(flotte_db, "table1", 2.4, 6.6, 0.96, 0.25)
Positions.insert_Pose(flotte_db, "table2", 1.15, 6.26, 0.76, -0.64)
Positions.insert_Pose(flotte_db, "table3", 1.86, 8.88, 0.27, -0.96)
Positions.insert_Pose(flotte_db, "bar", 4.5, 8.12, 0.95, -0.3)

Type.insert_Type(flotte_db, "Robotino", "Service", 20000)
Type.insert_Type(flotte_db, "Heron", "Service", 10000)
Type.insert_Type(flotte_db, "Turtlebot", "Service", 1000)
Type.insert_Type(flotte_db, "Caroita", "Preparateur", 500)
Type.insert_Type(flotte_db, "Accueil", "Accueil", -1)



subscribe(my_ip, port, "Initialisation/Envoi", 2)
subscribe(my_ip, port, "Commande/Envoi", 2)
subscribe(my_ip, port, "Ordre/Etat", 2)
subscribe(my_ip, port, "Robot/Ping", 2)

# Mode ecoute sur le topic de scan des nouveaux robots

# Si nouveau robot

	# Récupération des infos du message

	# Mise en BDD




############
### Main ###
############


# Lancement de L'IHM principale

#curses.wrapper(main)


#vérification des "ping" robot (25s)
pingRobots()

while 1:

	time.sleep(10)


# Ecoute des nouveaux clients

# Si nouveau client

	# Si robot serveur dispo

		# Message vers le robot pour emmener le/les clients a la table

# Ecoute des nouvelles commandes

# Si nouvelle commande

	# Si preparateur dispo

		# Message pour preparer la commande

# Ecoute des commandes a livrer

# Si commande a livrer

	# Si robot serveur dispo

		# Envoi message pour livrer la commande 
