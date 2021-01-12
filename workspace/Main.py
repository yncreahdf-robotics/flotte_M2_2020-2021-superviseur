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
import Article


# Import des librairies exterieures au projet


import time
import threading
import paho.mqtt.client as mqtt
import mysql.connector
import datetime



##########################
### Variables globales ###
##########################

timer=None
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
		if Type.Type_exists(typerobot):
			#TODO: mettre la position initiale du robot 
			if(Type.get_Type(typerobot)[0][2]=="Preparateur"):
				Robot.insert_Robot(iprobot, typerobot, Positions.get_Pose_by_name("bar")[0][0], "Idle", 0, datetime.datetime.now())
			else:
				Robot.insert_Robot(iprobot, typerobot, Positions.get_Pose_by_name("recharge")[0][0], "Idle", 0, datetime.datetime.now()) 

		# Si le type de robot n'existe pas encore on l'ajoute à la base des types
		else:
			#TODO: Lancer la fonction pour ajouter un type de robot dans la base de données à partir de l'IHM
			print("MESSAGE:  Type de robot inexistant")
		
	if msg.topic == "Commande/Envoi":
		print("MESSAGE:  Nouvelle commande")



	

	if msg.topic == "Robot/Ping": 

		iprobot = msg.payload.decode("utf-8")

		#print("MESSAGE:  Reception d'un ping : " + iprobot)

		confirmation = 0

		result = Robot.get_all_Robot()
	
		for robot in result:

			if robot[0] == iprobot:

				Robot.update_ping(robot[0])

				confirmation = 1

		if confirmation == 0:

			publish(my_ip, port, "Ping/Feedback", iprobot + "/" + "No", 2)

	#####################
	##	Topic Accueil  ##
	#####################

	if msg.topic == "Accueil/Client":

		NbrClient=msg.payload.decode("utf-8")[0]

		#	Mise à jour de la table accueillant les clients
		tablesLibres=Table.get_Table_Nbr_and_Status(NbrClient, "Free")

		if len(tablesLibres)!=0:
			Table.update_Table_status(tableLibres[0], Occupied)

			#	Assigne un robot pour guider les clients à la table choisie
			service=Robot.get_robot_by_role_and_status("Guide", "Idle")

			if len(service)!=0:
				#	On dit au robot de service choisi de guider les clients jusqu'à leur table
				Robot.update_status(service,"Occupied")
				publish(my_ip, port, "Service/Guide", str(service) , 2)

			else:
				print("MESSAGE: Pas de robot libre pour guider les nouveaux clients")

		else:
			print("MESSAGE:	Aucune table de libre")


	if msg.topic == "Accueil/Paiement":
		pass;
		#TODO: Libérer la table dans la base de données



	if msg.topic == "Accueil/GelLow":
		print("MESSAGE: Niveau de gel bas")


	#if msg.topic == "RobotCharles":

	#	print(msg.payload.decode("utf-8"))




	#########################
	##	Topic Préparateur  ##
	#########################

	#	Quand le préparateur a fini de préparer une commande
	if msg.topic == "Preparateur/Prepared":
		#time.sleep(5)

		#	On récupère l'IP du préparateur ayant terminé sa préparation
		preparateur = msg.payload.decode("utf-8").split("/")[0]

		#	On cherche le numéro de la commande prête (dans le message)
		CommandNbr = msg.payload.decode("utf-8").split("/")[1]

		# 	Mise de l'article préparé en "Prepared"
		ArticleID=Commande.get_Commande_with_status_and_commandNbr(CommandNbr,"Ordered")[0][0]
		Commande.update_Commande_status_by_article(ArticleID, "Prepared")
	
		#	On regarde si la commande complète est prête
		if (len(Commande.get_Commande_with_status_and_commandNbr(CommandNbr, "Ordered"))!=0):
			#Si tous les articles ne sont pas prêts on continue de préparer la commande
			publish(my_ip, port, "Preparateur/Prepare", str(preparateur) + "/" + str(CommandNbr) , 2)

		#	Si tous les articles sont prets on charge le robot ou on l'attend
		else:
			print("MESSAGE:	COMMANDE PRETE: " + CommandNbr)
			#	On met à jour l'état de la commande
			Table.update_status(CommandNbr,"Prepared")
			#	Le préparateur peut préparer une autre commande
			Robot.update_status(preparateur, "Idle")
			#	On cherche le robot de service qui s'occupe de la commande
			robot = Robot.get_robot_by_ActiveCommand_and_type(CommandNbr,"Service")[0][0]
			
			# Si le robot est déjà pret à être chargé (en attente)
			if Robot.get_robot_data(robot)[0][3] == "Pending" :
				#	Dire au préparateur de charger la commande
				publish(my_ip, port, "Preparateur/Charge", str(preparateur)+"/"+str(CommandNbr) , 2)

			#	Sinon on attend que le robot soit pret
			else: 
				print("MESSAGE:	COMMANDE PRETE: "+ str(CommandNbr) + " - ATTENTE DU ROBOT") 
				#TODO: refaire les changements d'état du préparateur pour plusieurs commandes
				#	Robot préparateur en "Pending"
				Robot.update_status(preparateur, "Pending")
			#SELECT * FROM Commande_tb;
 

		
 	
 	# Quand le preparateur a fini de charger 
	if msg.topic == "Preparateur/Charged":
		print("MESSAGE:	Article chargé")

		#récupération de l'ip du préparateur
		preparateur=msg.payload.decode("utf-8")

		#récupération du numéro de commande dont s'occupe le préparateur
		CommandNbr= Robot.get_robot_data(preparateur)[0][4]
		#recherche des articles non chargés de la commande
		remaining_articles=Commande.get_Commande_with_status_and_commandNbr(CommandNbr, "Prepared")
		#mise du premier article de la liste en chargé
		Commande.update_Commande_status_by_article(remaining_articles[0][0], "Charged" )
		#recherche des articles non chargés de la commande
		remaining_articles=Commande.get_Commande_with_status_and_commandNbr(CommandNbr, "Prepared")

		#recherche du robot de service sur lequel on charge la commande
		robot=Robot.get_robot_by_ActiveCommand_and_type(CommandNbr, "Service")[0][0]
		#	Si l'article est le dernier de la commande on envoie le départ du robot
		if len(remaining_articles)==0:
			print("MESSAGE: Commande chargée")
			
			#on cherche la table de la commande
			tableID=Table.get_Table_by_CommandNbr(CommandNbr)[0][0]
			#on cherche l'ID de la position de la table
			poseID=Table.get_Table_data(tableID)[0][2]
			#	robot en "Occupied"
			Robot.update_status(robot, "Occupied")
			# 	Commande en "Charged"
			Table.update_status(CommandNbr,"Charged")

			#	envoi de l'ordre au robot de livrer la commande à la table séléctionnée
			publish(my_ip, port, "Service/Go/Table", str(robot) + "/" + str(poseID),2)
		
		#	Sinon on continue de charger et on demande au robot de tourner d'un 8e de tour
		else:
			print("MESSAGE: Chargement de l'article suivant")
			#On dit au robot de service sur lequel on charge la commande de tourner 
			#TODO: voir si on tourne à chaque fois ou si on tourne une fois sur deux dans le cas de l'utilisation des 2 Nyrio pour charger le robot
			publish(my_ip , port, "Service/Turn", str(robot), 2)
			#On dit au préparateur de charger l'article suivant
			publish(my_ip , port, "Preparateur/Charge", str(preparateur)+"/"+str(CommandNbr), 2)

 	##############################
 	##	Topic Service et Guide  ##
 	##############################i
	if (msg.topic.split("/")[1]=="Arrived"):
		#Si le robot dit être arrivé, on met à jour sa position dans la base de données
		#On trouve d'abord le robot en question
		robot=msg.payload.decode("utf-8").split("/")[0]
		#On trouve ensuite la nouvelle position du robot
		position=msg.payload.decode("utf-8").split("/")[1]
		#On met à jour la position du robot
		Robot.update_position(robot,position)
		#Quand le robot arrive à la base de chargement des commandes
		if msg.topic == "Service/Arrived/Bar":
			
			print("MESSAGE: ROBOT ARRIVE A LA BASE DE CHARGEMENT")
			#print("ip: " + str(msg.payload.decode("utf-8")))
			CommandNbr=Robot.get_robot_data(robot)[0][4]
			print("Commande: "+ str(CommandNbr))

			#	Si la commande est prête le préparateur est en attente
			#	On utilise la position du robot qui nous envoie le message pour déterminer le préparateur utilisé
			print("preparateur: "+str(Robot.get_robot_by_ActiveCommand_and_type(CommandNbr,"Preparateur")[0][0]))
			preparateur=Robot.get_robot_by_ActiveCommand_and_type(CommandNbr,"Preparateur")[0][0]
			
			print("status: "+Robot.get_robot_data(preparateur)[0][3])
			if Robot.get_robot_data(preparateur)[0][3]=="Pending":
				#On lance le chargement de la commande
				Robot.update_status(preparateur[0],"Occupied")
				publish(my_ip, port, "Commande/Charge", preparateur[0] , 2)

			else:
		 		#	On fait attendre le robot jusqu'à ce que la commande soit prête
		 		print("MESSAGE: ROBOT DE SERVICE EN ATTENTE")
		 		robot=Robot.get_robot_by_ActiveCommand_and_type(CommandNbr,"Service")[0][0]
		 		Robot.update_status(robot, "Pending")

		#Quand le robot de service a livré
		if msg.topic == "Service/Arrived/Table":

			CommandNbr=Robot.get_robot_data(robot)[0][4]

			print("MESSAGE: Livraison en cours")
			time.sleep(5)
			print("MESSAGE: Commande livrée")

			#	Retour du robot à la base de recharge
			publish(my_ip, port, "Service/Go/Base", robot + "/" + str(Positions.get_Pose_by_name("recharge")[0][0]),2)
			
			#	robot en "Idle"
			Robot.update_status(robot, "Idle")

			#	Command en "Delivered"
			Commande.update_status(CommandNbr, "Delivered")

			#TODO:	Calcul du prix total de la table et mise en base de données

		if msg.topic == "Guide/Arrived":
			print("MESSAGE: Clients guidés jusqu'à la table")

			#	On libère le robot et on lui dit de retourner à sa base de recharge
			publish(my_ip, port, "Guide/Go/Base", robot, "recharge",2)
			Robot.update_status(robot, "Idle")



#Appel d'une fonction qui permet de recevoir un message

def subscribe(ip, port, topic, qos):

	client = mqtt.Client()

	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.connect(ip,port,65535)
	client.subscribe(topic, qos)
	client.loop_start()
	print("MQTT:     subscribe to "+topic)



#Appel d'une fonction qui permet d'envoyer un message

def publish(ip, port, topic, message, qos):

	client = mqtt.Client()

	client.connect(ip,port,65535)
	client.loop_start()
	client.publish(topic, message, qos)
	print("PUBLISH:  message sent to "+topic)



# Verifier que les robots en marche sont toujours en marche

def pingRobots():

	threading.Timer(30, pingRobots).start()	# Recommence toute les 30 sec

	InitBDDSuperviseur.use_db()


	result = Robot.get_all_Robot()
	#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	#print("PING:     Ping des robots ...")

	for robot in result:

		if (datetime.datetime.now() - robot[5]) > datetime.timedelta(seconds=30):
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("ROBOT:     Robot ", robot[1], " (", robot[0], ") ", " deconnecte")
			Robot.delete_Robot(robot[0])

		else:
			print("ROBOT:	", robot[1], " (", robot[0], ") ")


	#print("PING:     Ping terminé")
		
def command_loop():
	#Calcul des différentes données permettant la prise de décision
	Pending=Table.get_Table_by_Status("Pending")
	Ordered=Table.get_Table_by_Status("Ordered")
	Prepared=Table.get_Table_by_Status("Prepared")
	Delivered=Table.get_Table_by_Status("Delivered")
	Service=Robot.find_robot_by_role("Service")
	Preparateur=Robot.find_robot_by_role("Preparateur")
	Free_Service=Robot.find_robot_by_role_and_status("Service","Idle")
	Free_Preparateur=Robot.find_robot_by_role_and_status("Preparateur","Idle")

	#Affichage des données 
	print("=============================================")
	print("COMMANDE(S):")
	print("En attente:"+ str(len(Pending)))
	print("Commandée(s):"+ str(len(Ordered)))
	print("Preparée(s):"+ str(len(Prepared)))
	print("Terminée(s):"+ str(len(Delivered)))
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("ROBOT(S):")
	print("Service(s):"+ str(len(Service)))
	print("Preparateur(s):"+ str(len(Preparateur)))
	print("---------------------------------------------")
	print("ROBOT(S) LIBRE(S):")
	print("Service(s):"+ str(len(Free_Service)))
	print("Preparateur(s):"+ str(len(Free_Preparateur)))
	
	#Si une commande est en attente de préparation
	if(len(Pending)!=0 and len(Free_Preparateur)!=0):
		print("MESSAGE:	PREPARATION DE COMMANDE: "+str(Pending[1][0])+ "par Preparateur: "+ str(Free_Preparateur[0]))
		#La commande est en preparation
		Commande.update_status(Pending[0][0], "Ordered")
		#Mise en occupé du préparateur
		Robot.update_status(Free_Preparateur[0][0],"Occupied")
		#Mise à jour de la commande active du preparateur
		Robot.update_command(Free_Preparateur[0][0], Pending[0][0])
		#Envoi de l'ordre au preparateur
		publish(my_ip, port, "Preparateur/Prepare", Free_Preparateur[0][0] + "/" + str(Pending[0][0]) , 2)

	#Si une commande est preparee et qu'aucun robot de service ne s'en occupe et qu'un robot de service est libre
	if(len(Prepared)!=0 and len(Free_Service)!=0): #and len(Robot.get_robot_by_ActiveCommand_and_type(Prepared[0][0], Service))==0:
		#Mise en occupé du robot de service
		Robot.update_status(Free_Service[0][0],"Occupied")
		#Mise à jour de la commande active du robot de service
		Robot.update_command(Free_Service[0][0], Pending[0][0])
		#On envoi un robot de service pour aller la chercher
		publish(my_ip, port, "Service/Go/Bar", Free_Service[0][0] + "/" + str(Free_Preparateur[0][2]), 2)
	time.sleep(30)
'''
	#	Si une commande est en attente et qu'un robot de service et un préparateur sont libres, lancer la commande
	if(len(Commande.get_CommandNbr_with_status("Pending"))!=0 and len(Robot.find_robot_by_role_and_status("Service", "Idle"))!=0 and len(Robot.find_robot_by_role_and_status("Preparateur", "Idle"))!=0):
		
		print("MESSAGE: Une commande est en préparation")

		commande=Commande.get_CommandNbr_with_status("Pending")[0][0]
		print(commande)
		Commande.update_status(commande, "Ordered")

		listeRobots=Robot.find_robot_by_role_and_status("Service", "Idle")
		listePreparateurs = Robot.find_robot_by_role_and_status("Preparateur", "Idle")

		#	On choisit le robot de service qui va effectuer la commande 
		robotMissione = listeRobots[0]
		iprobot=robotMissione[0]
		Robot.update_command(iprobot, commande)
		Robot.update_status(iprobot, "Occupied")

		#	On choisit le préparateur qui va effectuer la commande
		preparateurMissione = listePreparateurs[0]
		ippreparateur=preparateurMissione[0]
		Robot.update_command(ippreparateur,commande)
		Robot.update_status(ippreparateur, "Occupied")

		destination=Positions.get_Pose_by_name("bar")[0][0] 
		#Robot.get_robot_data(ippreparateur)[0][2]

		print("PUBLISH:  Envoi d'un ordre a", iprobot)
		publish(my_ip, port, "Service/Go/Bar", iprobot + "/" + str(destination), 2)

		print("PUBLISH:  Envoi d'un ordre a", ippreparateur)
		publish(my_ip, port, "Preparateur/Prepare", ippreparateur + "/" + str(commande) , 2)

		return True
	time.sleep(30)
	return False
'''

######################
### Initialisation ###
######################


# Lancement IHM Initialisation


InitBDDSuperviseur.delete_flotte_db()

InitBDDSuperviseur.create_flotte_db()

InitBDDSuperviseur.create_all_tables()

Positions.insert_Pose("recharge", 0.0771479708922038, 0.3639684060492877, -0.23, 0.97)
Positions.insert_Pose("table1", 2.9226691810219827, 0.7380693324419132, 0.79, 0.6)
Positions.insert_Pose("table2", 2.001872215066296, 1.1748824989062503, -0.83, 0.56)
Positions.insert_Pose("table3", 3.508061809231884, 2.9028496618974104, -0.56, 0.83)
Positions.insert_Pose("bar", 5.74,0.95,-0.8,0.6)
#Positions.insert_Pose("tagne", -21.2689863214036, -1.0389461981502848, 0.62, 0.80)
Positions.insert_Pose("accueil", 0.15,3.55,-0.25,1)

Type.insert_Type("Robotino", "Service", 20000)
Type.insert_Type("Heron", "Service", 10000)
Type.insert_Type("Turtlebot", "Guide", 1000)
Type.insert_Type("Caroita", "Preparateur", 500)
Type.insert_Type("Accueil", "Accueil", -1)

Table.insert_Table(0, Positions.get_Pose_by_name("table1")[0][0], 2, "Free", 0)
Table.insert_Table(0, Positions.get_Pose_by_name("table2")[0][0], 2, "Free", 0)
Table.insert_Table(0, Positions.get_Pose_by_name("table3")[0][0], 2, "Free", 0)

Article.insert_Article("Coca", 1, 33, 4, 0, 0, 0, 0, 0)
Article.insert_Article("Wisky", 1, 33, 0, 1, 0, 0, 0, 0)
Article.insert_Article("Leffe", 1, 33, 0, 0, 4, 0, 0, 0)
Article.insert_Article("Eau", 1, 33, 0, 0, 0, 8, 0, 0)
Article.insert_Article("Jaggermeister", 1, 33, 4, 0, 0, 0, 2, 2)

subscribe(my_ip, port, "Initialisation/Envoi", 2)
subscribe(my_ip, port, "Commande/Envoi", 2)
subscribe(my_ip, port, "Service/#", 2)
subscribe(my_ip, port, "Preparateur/#",2)
subscribe(my_ip, port, "Robot/Ping",2)
subscribe(my_ip, port, "Accueil/#",2)
#subscribe(my_ip, port, "RobotCharles",2)

############
### Main ###
############


# 	Lancement de L'IHM principale

pingRobots()

while 1:
	command_loop()

	

	


############################
## Messages initiaux MQTT ##
############################

	#print("Yes! i receive the message :" , str(msg.payload))
	#print("message received ", msg.payload.decode("utf-8"))
	#print("message topic=",msg.topic)
	#print("message qos=",msg.qos)
	#print("message retain flag=",msg.retain)

	
	# Topic - Réception d'une commande
	'''
	if msg.topic == "Commande/Envoi":

		print("MESSAGE:  Nouvelle commande")

		CommandNbr=msg.payload.decode("utf-8")[0]

		# recherche du robot dispo (+le plus proche de la destination si possible)			
		listeRobots=Robot.find_robot_by_role_and_status("Service", "Idle")

		# Vérifier qu'il y a des robots de service disponibles
		if len(listeRobots)!=0:

			# Recherche d'un preparateur disponible
			listePreparateurs = Robot.find_robot_by_role_and_status("Preparateur", "Idle")

			# Vérifier que la liste n'est pas vide
			if len(listePreparateurs)!=0:

				print("MESSAGE: Commande en cours de préparation"
					)
				#	Commande Etat="Ordered"
				Commande.update_status(CommandNbr,"Ordered")

				#TODO: choisir un robot avec des critères plus poussés?
				#	On choisit le robot de service qui va effectuer la commande 
				robotMissione = listeRobots[0]
				iprobot=robotMissione[0]
				Robot.update_status(iprobot, "Occupied")

				#TODO: choisir un préparateur avec des critères plus poussés?
				#	On choisit le préparateur qui va effectuer la commande
				preparateurMissione = listePreparateurs[0]
				ippreparateur=preparateurMissione[0]
				Robot.update_status(ippreparateur, "Occupied")

				destination=Robot.get_robot_data(ippreparateur)[0][2]

				print("PUBLISH:  Envoi d'un ordre a", iprobot)
				publish(my_ip, port, "Service/Go/Bar", iprobot + "/" + CommandNbr, 2)

				print("PUBLISH:  Envoi d'un ordre a", ippreparateur)
				publish(my_ip, port, "Preparateur/Prepare", ippreparateur + "/" +  CommandNbr , 2)

			# Si aucun préparateurt n'est disponible
			else:
			#	Commande - Etat="Pending"
				print("MESSAGE: Commande en attente - Préparateur Indisponible")
				Commande.update_status(CommandNbr,"Pending")

		# Si aucun robot de service n'est disponible
		else:
		#TODO: METTRE LA COMMANDE EN ATTENTE: Entrer la commande dans la base de données Etat="Pending"
			print("MESSAGE: Commande en attente - Préparateur Indisponible")
			Commande.update_status(CommandNbr,"Pending")

	## Fin Commande/Envoi
	'''
