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
import Table
import Commande


# Import des librairies exterieures au projet


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

	######################
	##	Topic Généraux  ##
	######################

	# Topic - Connexion d'un nouveau robot
	if msg.topic == "Initialisation/Envoi":

		# Récupération de l'ip du robot et de son type
		iprobot = msg.payload.decode("utf-8").split("/")[0]
		typerobot = msg.payload.decode("utf-8").split("/")[1]

		print("MESSAGE:  Nouveau robot,", typerobot, " (", iprobot, "), mise en bdd")

		# Si le type existe on ajoute le robot à la liste des robots disponibles de la base de données
		if Type.Type_exists(mycursor, typerobot):
			#TODO: mettre la position initiale du robot
			Robot.insert_Robot(mycursor, flotte_db, iprobot, typerobot, "0, 0, 0, 0", "Idle", datetime.datetime.now())

		# Si le type de robot n'existe pas encore on l'ajoute à la base des types
		else:
			#TODO: Lancer la fonction pour ajouter un type de robot dans la base de données à partir de l'IHM
			print("MESSAGE:  Type de robot inexistant")
		

	# Topic - Réception d'une commande
	if msg.topic == "Commande/Envoi":

		print("MESSAGE:  Nouvelle commande")

		CommandNbr=msg.payload.decode("utf-8")[0]

		# recherche du robot dispo (+le plus proche de la destination si possible)			
		listeRobots=Robot.find_robot_by_role_and_status(mycursor,"Service", "Idle")

		# Vérifier qu'il y a des robots de service disponibles
		if len(listeRobots)!=0:

			# Recherche d'un preparateur disponible
			listePreparateurs = Robot.find_robot_by_role_and_status(mycursor,"Preparateur", "Idle")

			# Vérifier que la liste n'est pas vide
			if len(listePreparateurs)!=0:

				print("MESSAGE: Commande en cours de préparation"
					)
				#	Commande Etat="Ordered"
				Commande.update_status(mycursor,CommandNbr,"Ordered")

				#TODO: choisir un robot avec des critères plus poussés?
				#	On choisit le robot de service qui va effectuer la commande 
				robotMissione = listeRobots[0]
				iprobot=robotMissione[0]
				Robot.update_status(mycursor, iprobot, "Occupied")

				#TODO: choisir un préparateur avec des critères plus poussés?
				#	On choisit le préparateur qui va effectuer la commande
				preparateurMissione = listePreparateurs[0]
				ippreparateur=preparateurMissione[0]
				Robot.update_status(mycursor, ippreparateur, "Occupied")

				destination=Robot.get_robot_data(mycursor,ippreparateur)[2]

				print("PUBLISH:  Envoi d'un ordre a", iprobot)
				publish(my_ip, port, "Service/Go/Bar", iprobot + "/" + CommandNbr, 2)

				print("PUBLISH:  Envoi d'un ordre a", ippreparateur)
				publish(my_ip, port, "Preparateur/Prepare", ippreparateur + "/" +  CommandNbr , 2)

			# Si aucun préparateurt n'est disponible
			else:
			#	Commande - Etat="Pending"
				print("MESSAGE: Commande en attente - Préparateur Indisponible")
				Commande.update_status(mycursor,CommandNbr,"Pending")

		# Si aucun robot de service n'est disponible
		else:
		#TODO: METTRE LA COMMANDE EN ATTENTE: Entrer la commande dans la base de données Etat="Pending"
			print("MESSAGE: Commande en attente - Préparateur Indisponible")
			Commande.update_status(mycursor,CommandNbr,"Pending")

	## Fin Commande/Envoi

	if msg.topic == "Robot/Ping": 

		iprobot = msg.payload.decode("utf-8")

		print("MESSAGE:  Reception d'un ping : " + iprobot)

		confirmation = 0

		result = Robot.get_all_Robot(mycursor)
	
		for robot in result:

			if robot[0] == iprobot:

				Robot.update_ping(flotte_db, robot[0])

				confirmation = 1

		if confirmation == 0:

			publish(my_ip, port, "Ping/Feedback", iprobot + "/" + "No", 2)

	#####################
	##	Topic Accueil  ##
	#####################

	if msg.topic == "Accueil/Client":

		NbrClient=msg.payload.decode("utf-8")[0]

		#	Mise à jour de la table accueillant les clients
		tablesLibres=Table.get_Table_Nbr_and_Status(mycursor, NbrClient, "Free")

		if len(tablesLibres)!=0:
			Table.update_Table_status(mycursor, tableLibres[0], Occupied)

			#	Assigne un robot pour guider les clients à la table choisie
			service=Robot.get_robot_by_role_and_status(mycursor, "Service", "Idle")

			if len(service)!=0:
				#	On dit au robot de service choisi de guider les clients jusqu'à leur table
				Robot.update_status(mycursor,service,"Occupied")
				publish(my_ip, port, "Service/Guide", str(service) , 2)

			else:
				print("MESSAGE: Pas de robot libre pour guider les nouveaux clients")

		else:
			print("MESSAGE:	Aucune table de libre")


	if msg.topic == "Accueil/Paiement":
		pass;
		#TODO: Libérer la table dans la base de données



	#########################
	##	Topic Préparateur  ##
	#########################

	#	Quand le préparateur a fini de préparer une commande
	if msg.topic == "Preparateur/Prepared":

		print("MESSAGE: COMMANDE PRETE")

		CommandNbr=msg.payload.decode("utf-8")[1]
		#	On récupère l'IP du préparateur ayant terminé sa préparation
		preparateur= msg.payload.decode("utf-8")[0]

		#	On cherche la position du préparateur pour chercher le robot qui s'y trouve
		position=Robot.get_robot_data(mycursor,ippreparateur)[2]
		listeRobots = Robot.find_Robot_by_role_status_and_position(mycursor, "Service", "Pending", position)
		
		# Vérifier que la liste n'est pas vide
		if len(listeRobots)!=0 :
			print("MESSAGE: Robot trouve")
			robotMissione = listeRobots[0] #premier robot dispo dans la liste choisi
			ipRobotMissione = robotMissione[0]

			publish(my_ip, port, "Preparateur/Charge", str(ippreparateur) , 2)

			# 	Robot préparateur en "Occupied"
			Robot.update_status(mycursor, preparateur,"Occupied")

		#	Sinon on attend un robot 
		else: 
			print("MESSAGE: COMMANDE PRETE - ATTENTE D'UN ROBOT") 

			#TODO Robot préparateur en "Pending"
			Robot.update_status(mycursor, preparateur, "Pending")
			#TODO Commande en "Prepared"

		# 	Commande en "Prepared"
		Commande.update_status(mycursor, CommandNbr, "Prepared")
 	
 	# Quand le preparateur a fini de charger 
	if msg.topic == "Preparateur/Charged":

		preparateur=msg.payload.decode("utf-8")[0]
		CommandNbr=msg.payload.decode("utf-8")[1]
		remaining_articles=Commande.get_Commande_with_status_and_commandNbr(mycursor, CommandNbr, "Prepared")
		
		# 	Commande en "Charged"
		Commande.update_status_by_article(mycursor, remaining_articles[0], "Charged" )

		#	Recherche des articles restant à charger
		remaining_articles=Commande.get_Commande_with_status_and_commandNbr(mycursor, CommandNbr, "Prepared")

		#	Si l'article est le dernier de la commande on envoie le départ du robot
		if remaining_articles==0:
			print("MESSAGE: Commande chargée")
			listeRobot=Robot.find_Robot_by_role_status_and_position("Service","Pending",Robot.get_robot_data[2])
			robot=listeRobot[0]

			#	robot en "Occupied"
			Robot.update_status(mycursor, robot, "Occupied")

			publish(my_ip, port, "Service/Go/Table", robot + "/" + CommandNbr,2)
		
		#	Sinon on continue de charger et on demande au robot de tourner d'un 8e de tour
		else:
			print("MESSAGE: Chargement de l'article suivant")
			publish(my_ip , port, "Service/Turn", robot, 2)
			publish(my_ip , port, "Preparateur/Charge", preparateur, 2)

 	#####################
 	##	Topic Service  ##
 	#####################

	#Quand le robot arrive à la base de chargement des commandes
	if msg.topic == "Service/Arrived/Bar":
		
		print("MESSAGE: ROBOT ARRIVE A LA BASE DE CHARGEMENT")
		
		robot=msg.payload.decode("utf-8")[0]

		#	Si la commande est prête le préparateur est en attente
		#	On utilise la position du robot qui nous envoie le message pour déterminer le préparateur utilisé
		preparateur=Robot.find_Robot_by_role_status_and_position(mycursor, "Preparateur", "Pending", Robot.get_robot_data(mycursor, robot)[2])
		
		if Robot.get_robot_data(preparateur)[3]=="Pending":
			#On lance le chargement de la commande
			Robot.update_status(mycursor,preparateur[0],"Occupied")
			publish(my_ip, port, "Commande/Charge", preparateur[0] , 2)

		else:
	 		#	On fait attendre le robot jusqu'à ce que la commande soit prête
	 		robot=Robot.find_Robot_by_role_status_and_position(mycursor, "Service", "Occupied", Robot.get_robot_data(preparateur)[2])
	 		Robot.update_status(mycursor,robot[0], "Pending")

	#Quand le robot de service a livré
	if msg.topic == "Service/Arrived/Table":

		CommandNbr=msg.payload.decode("utf-8")[1]
		robot=msg.payload.decode("utf-8")[0]

		print("MESSAGE: Livraison en cours")
		time.sleep(30)
		print("MESSAGE: Commande livrée")

		#	Retour du robot à la base de recharge
		publish(my_ip, port, "Service/Go/Base", robot + "recharge",2)
		
		#	robot en "Idle"
		Robot.update_status(mycursor, robot, "Idle")

		#	Command en "Delivered"
		Command.update_status(mycursor, CommandNbr, "Delivered")

		#TODO:	Calcul du prix total de la table et mise en base de données

	if msg.topic == "Service/Guided":
		print("MESSAGE: Clients guidés jusqu'à la table")

		robot=msg.payload.decode("utf-8")[0]

		#	On libère le robot et on lui dit de retourner à sa base de recharge
		publish(my_ip, port, "Service/Go/Base", robot, "recharge",2)
		Robot.update_status(mycursor, robot, "Idle")



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

Positions.insert_Pose(flotte_db, "recharge", 0.0771479708922038, 0.3639684060492877, -0.23, 0.97)
Positions.insert_Pose(flotte_db, "table1", 2.9226691810219827, 0.7380693324419132, 0.79, 0.6)
Positions.insert_Pose(flotte_db, "table2", 2.001872215066296, 1.1748824989062503, -0.83, 0.56)
Positions.insert_Pose(flotte_db, "table3", 3.508061809231884, 2.9028496618974104, -0.56, 0.83)
Positions.insert_Pose(flotte_db, "bar", 5.475816980908464, 0.8688550177547738, 0.95, -0.3)
Positions.insert_Pose(flotte_db, "tagne", -21.2689863214036, -1.0389461981502848, 0.62, 0.80)

Type.insert_Type(flotte_db, "Robotino", "Service", 20000)
Type.insert_Type(flotte_db, "Heron", "Service", 10000)
Type.insert_Type(flotte_db, "Turtlebot", "Service", 1000)
Type.insert_Type(flotte_db, "Caroita", "Preparateur", 500)
Type.insert_Type(flotte_db, "Accueil", "Accueil", -1)

Table.insert_Table(mycursor, 0, Positions.get_Pose_by_name(mycursor, "table1")[0][0], 2, "Free", 0)
Table.insert_Table(mycursor, 0, Positions.get_Pose_by_name(mycursor, "table2")[0][0], 2, "Free", 0)
Table.insert_Table(mycursor, 0, Positions.get_Pose_by_name(mycursor, "table3")[0][0], 2, "Free", 0)

subscribe(my_ip, port, "Initialisation/Envoi", 2)
subscribe(my_ip, port, "Commande/Envoi", 2)
subscribe(my_ip, port, "Service/#", 2)
subscribe(my_ip, port, "Preparateur/#",2)
subscribe(my_ip, port, "Robot/ping",2)
subscribe(my_ip, port, "Accueil/#",2)

############
### Main ###
############


# 	Lancement de L'IHM principale

#	curses.wrapper(main)

pingRobots()

while 1:
	
	#	Si une commande est en attente et qu'un robot de service et un préparateur sont libres, lancer la commande
	if(len(Commande.get_CommandNbr_with_status(mycursor,"Pending"))!=0 and len(Robot.get_robot_by_role_and_status(mycursor, "Service", "Idle"))!=0 and len(Robot.get_robot_by_role_and_status(mycursor, "Preparateur", "Idle"))!=0):
		
		print("MESSAGE: Une commande est en préparation")

		commande=Commande.get_CommandNbr_with_status(mycursor,"Pending")[0]
		Commande.update_Commande_Status(mycursor, commande, "Ordered")

		#TODO: choisir un robot avec des critères plus poussés?
		#	On choisit le robot de service qui va effectuer la commande 
		robotMissione = listeRobots[0]
		iprobot=robotMissione[0]
		Robot.update_status(mycursor, iprobot, "Occupied")

		#TODO: choisir un préparateur avec des critères plus poussés?
		#	On choisit le préparateur qui va effectuer la commande
		preparateurMissione = listePreparateurs[0]
		ippreparateur=preparateurMissione[0]
		Robot.update_status(mycursor, ippreparateur, "Occupied")

		destination=Robot.get_robot_data(mycursor,ippreparateur)[2]

		print("PUBLISH:  Envoi d'un ordre a", iprobot)
		publish(my_ip, port, "Service/Go/Bar", iprobot + "/" + destination, 2)

		print("PUBLISH:  Envoi d'un ordre a", ippreparateur)
		publish(my_ip, port, "Preparateur/Prepare", ippreparateur + "/" + commande , 2)

	time.sleep(60)



#TODO 
# Ecoute des nouveaux clients

# Si nouveau client

	# Si robot serveur dispo

		# Message vers le robot pour emmener le/les clients a la table

# Ecoute des nouvelles commandes


############################
## Messages initiaux MQTT ##
############################

	#print("Yes! i receive the message :" , str(msg.payload))
	#print("message received ", msg.payload.decode("utf-8"))
	#print("message topic=",msg.topic)
	#print("message qos=",msg.qos)
	#print("message retain flag=",msg.retain)