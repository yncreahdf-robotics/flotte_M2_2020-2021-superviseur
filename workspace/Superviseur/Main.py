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
import Bouteille
import Recette

# Import des librairies exterieures au projet


import time
import threading
import paho.mqtt.client as mqtt
import mysql.connector
import datetime





##########################
### Variables globales ###
##########################
global tentative
#global service_turns
tentative = 0
#service_turns = 0 

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
article_count=0


############
### Defs ###
############


def on_connect(client, userdata, flags, rc):

	#print("MQTT:     Connected with result code "+str(rc))
	if rc==0:
		#print("MQTT:     connection ok")
		pass
	else:
		print("MQTT:     Erreur de connexion")
		#pass

	


def on_disconnect(client, userdata, rc):

	print("Client Got Disconnected")


def on_message(client, userdata, msg):

	######################
	##	Topic Généraux  ##
	######################
	print(msg.topic)
	print(msg.payload.decode("utf-8"))

	# Topic - Connexion d'un nouveau robot
	if msg.topic == "Initialisation/Envoi":

		# Récupération de l'ip du robot et de son type
		iprobot = msg.payload.decode("utf-8").split("/")[0]
		typerobot = msg.payload.decode("utf-8").split("/")[1]

		print("MESSAGE:  Nouveau robot,", typerobot, " (", iprobot, ")")

		# Si le type existe on ajoute le robot à la liste des robots disponibles de la base de données
		if Type.Type_exists(typerobot):
			add_robot_user(iprobot)
			#TODO: mettre la position initiale du robot 
			if(Type.get_Type(typerobot)[0][2]=="Preparateur"):
				Robot.insert_Robot(iprobot+"/1", typerobot+"/Melangeur", Positions.get_Pose_by_name("bar")[0][0], "Idle", 0, datetime.datetime.now())
				Robot.insert_Robot(iprobot+"/2", typerobot+"/Manipulateur", Positions.get_Pose_by_name("bar")[0][0], "Idle", 0, datetime.datetime.now())
				#envoi du message de lancement des différents programmes du Préparateur
				publish(my_ip, port, "Preparateur/Start", iprobot, 2)
			else:
				Robot.insert_Robot(iprobot, typerobot, 0, "Idle", 0, datetime.datetime.now()) 

		# Si le type de robot n'existe pas encore on l'ajoute à la base des types
		else:
			#TODO: Lancer la fonction pour ajouter un type de robot dans la base de données à partir de l'IHM
			print("MESSAGE:  Type de robot inexistant")
		
	if msg.topic == "Commande/Envoi":
		#pass
		print("MESSAGE:  Nouvelle commande")



	

	if msg.topic == "Robot/Ping": 
		#	On cherche l'ip du robot qui nous envoie le message
		iprobot = msg.payload.decode("utf-8").split("/")[0]

		#	si le robot transmet ses niveaux de batterie et son état de charge on les récupère
		if (len(msg.payload.decode("utf-8").split("/"))>1):
			battery=msg.payload.decode("utf-8").split("/")[1]
			charge_status=msg.payload.decode("utf-8").split("/")[2]
			Robot.update_battery(iprobot,battery,charge_status)
			#print(msg.payload.decode("utf-8"))
			if (float(battery)<10 and charge_status=="Unpluged" and Robot.get_robot_data(iprobot)[0][3]=="Idle"):
				publish(my_ip, port, "Service/Go/Base", iprobot+"/"+str(Positions.get_Pose_by_name("recharge")[0][0]), 2)
				publish(my_ip, port, "Guide/Go/Base", iprobot+"/"+str(Positions.get_Pose_by_name("recharge")[0][0]), 2)
		#print("MESSAGE:  Reception d'un ping : " + iprobot)

		confirmation = 0

		result = Robot.get_all_Robot()
	
		for robot in result:

			if robot[0].split("/")[0] == iprobot:

				Robot.update_ping(robot[0])

				confirmation = 1

		if confirmation == 0:

			publish(my_ip, port, "Ping/Feedback", iprobot + "/" + "No", 2)



	#####################
	##	Topic Accueil  ##
	#####################

	if msg.topic == "Accueil/Client":

		NbrClient=msg.payload.decode("utf-8")[0]

		#	On cherche si une table est libre avec le bon nombre de places
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


	#if msg.topic == "Accueil/Paiement":
	#	CommandNbr=msg.payload.decode("utf-8").split("/")[1]
	#	table=Table.get_Table_by_CommandNbr(CommandNbr)
	#	#Libérer la table dans la base de données
	#	Table.update_status(table, "Free")
	#	Table.update_command(0)
		



	if msg.topic == "Accueil/GelLow":
		#print("MESSAGE: Niveau de gel bas")
		pass


	#########################
	##	Topic Préparateur  ##
	#########################
	'''if msg.topic == "Commande/Reset":
		Commande.update_status(1,"Pending")
		Table.update_Table_status(2,"Pending")
'''
	#	Quand le préparateur a fini de préparer une commande
	if msg.topic == "Preparateur/Prepared":
		global tentative
		tentative = 0
		print("MESSAGE:	ARTICLE PREPARE")
		#	On récupère l'IP du préparateur ayant terminé sa préparation
		preparateur = msg.payload.decode("utf-8")

		#	On cherche le numéro de la commande prête (La commande active du robot melangeur)
		CommandNbr=Robot.get_robot_data(preparateur+"/1")[0][4]

		# 	Mise de l'article préparé en "Prepared"
		ArticleID=Commande.get_Commande_with_status_and_commandNbr(CommandNbr,"Ordered")[0][0]
		Commande.update_Commande_status_by_article(ArticleID, "Prepared")
	
		#	On regarde si la commande complète est prête
		CommandeIDlist=Commande.get_Commande_with_status_and_commandNbr(CommandNbr, "Ordered")
		#print(str(len(CommandeIDlist)))
		if (len(CommandeIDlist)!=0):
			#Si tous les articles ne sont pas prêts on continue de préparer la commande
			publish(my_ip, port, "Preparateur/Prepare", str(preparateur) + "/" + str(CommandNbr) , 2)

		#	Si tous les articles sont prets on charge le robot ou on l'attend
		else:
			print("MESSAGE:	COMMANDE PRETE: " + str(CommandNbr))
			#On met la Commande en préparée
			Table.update_Table_status(Table.get_Table_by_CommandNbr(CommandNbr)[0][0],"Prepared")
			#	Le préparateur peut préparer une autre commande
			Robot.update_status(preparateur+"/1", "Idle")

			# 	On attribue la commande au Manipulateur du même préparateur et on libère le Mélangeur
			Robot.update_command(preparateur+"/1", 0)
			Robot.update_command(preparateur+"/2", CommandNbr)

			#	On cherche le robot de service qui s'occupe de la commande
			#print(Robot.get_robot_by_ActiveCommand_and_type(CommandNbr,"Service"))
			if (len(Robot.get_robot_by_ActiveCommand_and_type(CommandNbr,"Service"))!=0):
				#On détermine le robot en charge de la commande
				robot = Robot.get_robot_by_ActiveCommand_and_type(CommandNbr,"Service")[0][0]
			
				# Si le robot est déjà pret à être chargé (en attente)
				if (len(robot)!=0 and Robot.get_robot_data(robot)[0][3] == "Pending") :
					#	Dire au préparateur de charger la commande
					publish(my_ip, port, "Preparateur/Charge", str(preparateur)+"/"+str(CommandNbr) , 2)

				#	Sinon = Si un robot est attribué à la commande  mais n'est pas encore arrivé
				else: 
					print("MESSAGE:	COMMANDE PRETE: "+ str(CommandNbr) + " - ATTENTE DU ROBOT") 
					#TODO: refaire les changements d'état du préparateur pour plusieurs commandes
					#	Robot préparateur en "Pending"
					Robot.update_status(preparateur+"/2", "Pending")
				#SELECT * FROM Commande_tb;
	 
			else: 
				# 	Si aucun robot de service ne se charge de la commande on attend qu'un robot soit attribué
				print("MESSAGE:	COMMANDE PRETE - AUCUN ROBOT DISPONIBLE")
				Robot.update_status(preparateur+"/2", "Pending")
		
 	
 	# Quand le preparateur a fini de charger 
	if msg.topic == "Preparateur/Charged":
		print("MESSAGE:	Article chargé")

		#récupération de l'ip du préparateur
		preparateur=msg.payload.decode("utf-8")
		#print(Robot.get_robot_data(preparateur+"/2"))
		#récupération du numéro de commande dont s'occupe le préparateur
		CommandNbr= Robot.get_robot_data(preparateur+"/2")[0][4]

		#recherche des articles non chargés de la commande
		remaining_articles=Commande.get_Commande_with_status_and_commandNbr(CommandNbr, "Prepared")
		#mise du premier article de la liste en chargé
		Commande.update_Commande_status_by_article(remaining_articles[0][0], "Charged" )
		#recherche des articles non chargés de la commande
		remaining_articles=Commande.get_Commande_with_status_and_commandNbr(CommandNbr, "Prepared")

		#recherche du robot de service sur lequel on charge la commande
		#robot=Robot.get_robot_by_ActiveCommand_and_type(CommandNbr, "Service")[0][0]

		#recherche du robot en fonction du poids
		poids_total = Article.total_weight_of_an_order(CommandNbr)
		print(poids_total)
		#On selectionne les robots disponibles
		robots_candidats=robot=Robot.get_robot_by_ActiveCommand_and_type(CommandNbr, "Service")
		for i in range (len(robots_candidats)):
			print(robots_candidats[i])
			if (Robot.get_robot_weight_capacity(i[0])>=poids_total and Robot.get_robot_weight_capacity(i[0])>Robot.get_robot_weight_capacity(robot)):
				robot=robots_candidats[i]
		print(robot)



		
		#	Si l'article est le dernier de la commande on envoie le départ du robot
		if len(remaining_articles)==0:
			print("MESSAGE: Commande chargée")
			#global service_turns
			#service_turns=0
			
			#on cherche la table de la commande
			tableID=Table.get_Table_by_CommandNbr(CommandNbr)[0][0]
			#on cherche l'ID de la position de la table
			poseID=Table.get_Table_data(tableID)[0][2]
			#	robot en "Occupied"
			Robot.update_status(robot, "Occupied")
			#	manipulateur libre
			Robot.update_status(preparateur+"/2","Idle")
			Robot.update_command(preparateur+"/2",0)
			# 	Commande en "Charged"
			Table.update_Table_status(tableID,"Charged")

			#	envoi de l'ordre au robot de livrer la commande à la table séléctionnée
			publish(my_ip, port, "Service/Go/Table", str(robot) + "/" + str(poseID),2)
		
		#	Sinon on continue de charger et on demande au robot de tourner d'un 8e de tour
		else:
			#article_count+=1
			print("MESSAGE: Chargement de l'article suivant")
			#On dit au robot de service sur lequel on charge la commande de tourner 
			#if(service_turns%2==0):
			publish(my_ip , port, "Service/Turn", str(robot), 2)
			#On dit au préparateur de charger l'article suivant
			publish(my_ip , port, "Preparateur/Charge", str(preparateur)+"/"+str(CommandNbr), 2)


	if msg.topic=="Preparateur/Error":
		preparateur=msg.payload.decode("utf-8").split("/")[0]
		melangeur=preparateur+"/1"
		CommandNbr=Robot.get_robot_data(melangeur)[0][4]
		print("!!!!!!!	ERREUR	!!!!!!!!!")
		codeError=int(msg.payload.decode("utf-8").split("/")[1])
		if(codeError==1):	#obstable gobelet
			print("Erreur 1 : obstacle gobelet")
			tentative += 1
			if (tentative <=3):
				publish(my_ip, port, "Preparateur/Prepare", preparateur + "/" + str(CommandNbr), 2)
			else : 
				Robot.update_status(preparateur+"/1","Maintenance")

			
		if(codeError==2):	#gobelet absent
			print("Erreur 2 : absence gobelet")
			tentative = tentative+1
			if (tentative <3):
				publish(my_ip, port, "Preparateur/Prepare", preparateur + "/" + str(CommandNbr), 2)
			else : 
				Robot.update_status(preparateur+"/1","Maintenance")



		if(codeError==3):
			Robot.update_status(preparateur+"/1","Maintenance")	
			print("Erreur 4 : mise en maintenance")

 	##############################
 	##	Topic Service et Guide  ##
 	##############################i
	if (msg.topic.split("/")[1]=="Arrived"):
		#Si le robot dit être arrivé, on met à jour sa position dans la base de données
		#On trouve d'abord le robot en question
		robot=msg.payload.decode("utf-8").split("/")[0]
		#On trouve ensuite la nouvelle position du robot
		position=msg.payload.decode("utf-8").split("/")[1]
		print(position)
		#On met à jour la position du robot
		Robot.update_position(robot,position)
		#Quand le robot arrive à la base de chargement des commandes
		if msg.topic == "Service/Arrived/Bar":
			
			print("MESSAGE: ROBOT ARRIVE AU BAR")
			#print("ip: " + str(msg.payload.decode("utf-8")))
			CommandNbr=Robot.get_robot_data(robot)[0][4]
			print("Commande: "+ str(CommandNbr))

			#preparateur=Robot.find_robot_by_CommandNbr_and_position(CommandNbr,position)[0][0]

			if (len(Robot.find_robot_by_CommandNbr_and_status(CommandNbr,"Pending"))!=0):
				#On lance le chargement de la commande
				print("MESSAGE: DEBUT CHARGEMENT")
				manipulateur=Robot.find_robot_by_CommandNbr_and_status(CommandNbr,"Pending")
				print(manipulateur)
				Robot.update_status(manipulateur,"Occupied")
				publish(my_ip, port, "Preparateur/Charge", str(manipulateur[0][0].split("/")[0]) + "/" + str(CommandNbr) , 2)

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
			Robot.update_command(robot,0)
			table=Table.get_Table_by_CommandNbr(CommandNbr)
			position=Table.get_Table_data(Table)[0][2]
			#	mise à jour de la dernière position du robot
			Robot.update_position(robot,position)

			#	Command en "Delivered"
			Commande.update_status(CommandNbr, "Delivered")
			Table.update_Table_status(Table.get_Table_by_CommandNbr(CommandNbr)[0][0],"Delivered")

		if msg.topic == "Guide/Arrived":
			robot=msg.payload.decode('utf-8').split("/")[0]
			position = msg.payload.decode('utf-8').split("/")[1]
			print("MESSAGE: Clients guidés")

			#	mise à jour de la dernière position du robot
			Robot.update_position(robot,position)
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
	#print("MQTT:     subscribe to "+topic)



#Appel d'une fonction qui permet d'envoyer un message

def publish(ip, port, topic, message, qos):

	client = mqtt.Client()

	client.connect(ip,port,65535)
	client.loop_start()
	client.publish(topic, message, qos)
	#print("PUBLISH:  message sent to "+topic)



# Verifier que les robots en marche sont toujours en marche

def pingRobots():

	threading.Timer(10, pingRobots).start()	# Recommence toute les 30 sec

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
			pass
			#print("ROBOT:	", robot[1], " (", robot[0], ") ")


	#print("PING:     Ping terminé")
		
# creer un utilisateur pour le robot pour qu'il se connecte à la base de données
def add_robot_user(iprobot):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		mycursor=flotte_db.cursor()
		
		requete1="CREATE USER IF NOT EXISTS'robot'@'"+iprobot+"' IDENTIFIED WITH mysql_native_password BY 'robot'" # WITH mysql_native_password 
		requete2="GRANT SELECT ON flotte_db.* TO 'robot'@'"+ iprobot+ "'"
		mycursor.execute("USE flotte_db")
		mycursor.execute(requete1)
		mycursor.execute(requete2)
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))



def command_loop():
	#Calcul des différentes données permettant la prise de décision
	Pending=Table.get_Table_by_Status("Pending")
	Ordered=Table.get_Table_by_Status("Ordered")
	Prepared=Table.get_Table_by_Status("Prepared")
	Delivered=Table.get_Table_by_Status("Delivered")
	NbrPending=Commande.get_commande_Nbr_status("Pending")
	NbrOrdered=Commande.get_commande_Nbr_status("Ordered")
	NbrPrepared=Commande.get_commande_Nbr_status("Prepared")
	Service=Robot.find_robot_by_role("Service")
	Guide=Robot.find_robot_by_role("Guide")
	Melangeur=Robot.find_robot_by_role("Melangeur")
	Manipulateur=Robot.find_robot_by_role("Manipulateur")
	Free_Service=Robot.find_robot_by_role_and_status("Service","Idle")
	Free_Guide=Robot.find_robot_by_role_and_status("Guide","Idle")
	Free_Melangeur=Robot.find_robot_by_role_and_status("Melangeur","Idle")
	Free_Manipulateur=Robot.find_robot_by_role_and_status("Manipulateur","Idle")

	#Affichage des données 
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("================ COMMANDE(S) ================")
	print("En attente:"+ str(len(Pending))+"		"+"Nbre d'article:"+str(len(NbrPending)))
	print("Commandée(s):"+ str(len(Ordered))+"		"+"Nbre d'article:"+str(len(NbrOrdered)))
	print("Preparée(s):"+ str(len(Prepared))+"		"+"Nbre d'article:"+str(len(NbrPrepared)))
	print("Terminée(s):"+ str(len(Delivered)))
	#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("================= ROBOT(S) ==================")
	print("Service(s):"+ str(len(Service)))



	print("Guide(s):"+str(len(Guide)))
	print("Melangeur(s):"+ str(len(Melangeur)))
	print("Manipulateur(s):"+ str(len(Manipulateur)))
	#print("---------------------------------------------")
	print("============ ROBOT(S) LIBRE(S) ==============")
	print("Service(s):"+ str(len(Free_Service)))
	print("Guide(s):"+str(len(Free_Guide)))
	print("Melangeur(s):"+ str(len(Free_Melangeur)))
	print("Manipulateur(s):"+ str(len(Free_Manipulateur)))
	
	#Si une commande est en attente de préparation
	if(len(Pending)!=0 and len(Free_Melangeur)!=0):
		print("MESSAGE:	PREPARATION DE COMMANDE: "+ str(Table.get_Table_data(Pending[0][0])[0][1]))#+ " par Preparateur: "+ str(Free_Melangeur[0]))
		
		#La commande est en preparation
		CommandNbr=Table.get_Table_data(Pending[0][0])[0][1]
		Commande.update_status_when_status(CommandNbr,"Pending" ,"Ordered")
		Table.update_Table_status(Pending[0][0],"Ordered")
		
		#Mise en occupé du préparateur
		Robot.update_status(Free_Melangeur[0][0],"Occupied")
		#Mise à jour de la commande active du preparateur
		Robot.update_command(Free_Melangeur[0][0], CommandNbr)
		
		#Envoi de l'ordre au preparateur
		publish(my_ip, port, "Preparateur/Prepare", Free_Melangeur[0][0].split("/")[0] + "/" + str(CommandNbr), 2)


	#Si une commande est preparee et qu'aucun robot de service ne s'en occupe et qu'un robot de service est libre
	if(len(Prepared)!=0 and len(Free_Service)!=0 and len(Robot.get_robot_by_ActiveCommand_and_type(Prepared[0][0], "Service"))==0):
		#Mise en occupé du robot de service
		Robot.update_status(Free_Service[0][0],"Occupied")
		#Mise à jour de la commande active du robot de service
		Robot.update_command(Free_Service[0][0], Table.get_Table_data(Prepared[0][0])[0][1])
		#On envoi un robot de service pour aller la chercher
		publish(my_ip, port, "Service/Go/Bar", Free_Service[0][0] + "/" + str(Positions.get_Pose_by_name("bar")[0][0]), 2)
		print("MESSAGE: Robot go to bar")

	time.sleep(10)

######################
### Initialisation ###
######################


# Lancement IHM Initialisation

InitBDDSuperviseur.create_flotte_db()

InitBDDSuperviseur.create_all_tables()

Positions.insert_Pose("table1", 3.30, 1.57, 0.05, -0.99)
Positions.insert_Pose("table2", 1.64, 1.26, 0.99, 0.03)
Positions.insert_Pose("table3", 2.56, 3.56, 0.91, -0.41)
Positions.insert_Pose("bar", 4.92, 2.77, 0.72, 0.69)
#Positions.insert_Pose("tagne", -21.2689863214036, -1.0389461981502848, 0.62, 0.80)
Positions.insert_Pose("accueil", 0.15,3.55,-0.25,1)

Type.insert_Type("Robotino", "Service", 20000)
Type.insert_Type("Heron", "Service", 10000)
Type.insert_Type("Turtlebot", "Guide", 1000)
Type.insert_Type("Caroita", "Preparateur", 500)
Type.insert_Type("Caroita/Melangeur", "Melangeur", 500)
Type.insert_Type("Caroita/Manipulateur", "Manipulateur", 500)
Type.insert_Type("Accueil", "Accueil", -1)

Table.insert_Table(0, Positions.get_Pose_by_name("table1")[0][0], 2, "Free", 0)
Table.insert_Table(0, Positions.get_Pose_by_name("table2")[0][0], 2, "Free", 0)
Table.insert_Table(0, Positions.get_Pose_by_name("table3")[0][0], 2, "Free", 0)


Bouteille.insert_Bouteille("Eau",25,7)
Bouteille.insert_Bouteille("Jagger Meister", 25, 1)
Bouteille.insert_Bouteille("Crazy Tigger", 75, 2)
Bouteille.insert_Bouteille("Sirop de Cerise", 75, 3)
Bouteille.insert_Bouteille("Badoit Rouge", 75, 4)
Bouteille.insert_Bouteille("Grenadine", 25, 5)


Bouteille.insert_Bouteille("Pas de bouteille",0,0)
Bouteille.update_ID("Pas de bouteille", 0)

Recette.insert_Recette("JaggerBomb", 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0)
Recette.insert_Recette("Grenadine", 5, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0)
Recette.insert_Recette("Eau Finement Pétillante", 4, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0)

Article.insert_Article("JaggerBomb", 1, 33, 1)
Article.insert_Article("Grenadine", 1, 33, 2)
Article.insert_Article("Eau Finement Pétillante", 1, 33, 3)

subscribe(my_ip, port, "Initialisation/#", 2)
subscribe(my_ip, port, "Commande/#", 2)
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

	

