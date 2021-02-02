# -*- coding: utf-8 -*-

###############
### Imports ###
###############

# Import des fichiers .py propre au projet

import IHM
import Robot
import Positions
import Type
import Table
import Commande
import Article
import InitBDDSuperviseur
import IPFinder

# Import des librairies exterieures au projet

import curses
import time
import paho.mqtt.client as mqtt
import mysql.connector
import threading
import datetime


##########################
### Variables globales ###
##########################

#	gets supervisor's IP using the host file
hosts = open('/etc/hosts','r')
for line in hosts:
	splitted_line=line.split()
	try:
		if splitted_line[1]=="supIP":
			ipsuperviseur = splitted_line[0]
	except IndexError:
		pass			
print (ipsuperviseur)	

#	TCP port used for MQTT	
port = 1883


menu_accueil = ["Preparateur", "Service", "Commande", "Return Trip","Libérez Robots", "Choix Robot"]
menu_preparateur = ["Preparateur/Prepare", "Preparateur/Charge", "Preparateur/Charged", "Fin de Maintenance", "Back"]
menu_service = ["Service/Go/Accueil", "Service/Go/Table1", "Service/Turn", "Service/Go/Bar", "Service/Go/Recharge", "Back"]
menu_returntrip = ["ReturnTrip Table1", "ReturnTrip Table2", "ReturnTrip Table3", "ReturnTrip Recharge", "Back"]
menu_choix_robot = ["Robotino", "Kobuki","Heron"]
menu_commande = ["Nouvelle Commande", "Commande de plusieurs articles","Supprimer commande unique", "Supprimer commande multiple","Back"]
menu_liberez_robots = ["Libérez Robotino","Libérez TurtleBot","Libérez Heron","Libérez Mélangeur","Libérez Manipulateur","Free Dobby","Back"]

############
### Defs ###
############

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


	if msg.topic == "Initialisation/Type":

		print("ip du robot" + msg.payload.decode("utf-8").split("/")[0])
		print("type de robot" + msg.payload.decode("utf-8").split("/")[1])



#Appel d'une fonction qui permet de recevoir un message

def subscribe(ip, port, topic, qos):

	client = mqtt.Client()

	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.connect(ip,port,65535)
	client.subscribe(topic, qos)
	client.loop_start()
	print("subscribed to "+topic)


#Appel d'une fonction qui permet d'envoyer un message

def publish(ip, port, topic, message, qos):

	client = mqtt.Client()

	client.connect(ip,port,65535)
	client.loop_start()
	client.publish(topic, message, qos)
	print("message sent to "+topic)


def main(stdscr):
	global CommandNbr
	CommandNbr=1

	InitBDDSuperviseur.use_db()
          
	menu=menu_accueil

	titre_menu = "MENU ACCUEIL (Robotino / 192.168.1.103)"

	robot_choisi = "Robotino"

	ip_choisie = "192.168.1.103"

	#turn off cursor blinking
	curses.curs_set(0)

	#color scheme for selected row
	curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)

	#specify the current selected row
	current_row = 0

	#print the menu
	IHM.print_menu(stdscr, current_row, menu, "MENU ACCUEIL (Robotino / 192.168.1.103)")
	

	#create_command_db()
	#check_command_db()
	#create_command_tb()
	#check_command_tb()



	while 1:
		key=stdscr.getch()

		# 	monte si la flèche du haut est pressée
		if key == curses.KEY_UP and current_row>0:
			current_row -= 1
		
		#	descend si la flèche du bas est pressée
		elif key == curses.KEY_DOWN and current_row < len(menu)-1:
			current_row +=1

		#	sort du menu si la touche echap est pressée
		elif key == 27:
			break

		#	valide le choix si la touche entrée est pressée
		elif key in [10,13]:
			stdscr.clear()
			stdscr.refresh()




#### Preparateur ####


			if menu[current_row] == "Preparateur":
				menu = menu_preparateur
				current_row = 0


			elif menu[current_row] == "Preparateur/Prepare":
				ippreparateur="192.168.1.7"
				#Commande.update_status(1, "Ordered")
				Robot.update_status(ippreparateur+"/1","Occupied")
				Robot.update_command(ippreparateur+"/1",1)
				publish(ipsuperviseur, port, "Preparateur/Prepare",ippreparateur + "/1", 2)



			elif menu[current_row] == "Preparateur/Charge":
				ippreparateur="192.168.1.7"
				Robot.update_status(ippreparateur+"/2","Occupied")
				Robot.update_command(ippreparateur+"/2",1)
				publish(ipsuperviseur, port, "Preparateur/Charge",ippreparateur + "/1", 2)

			elif menu[current_row] == "Preparateur/Charged":
				ippreparateur="192.168.1.7"
				publish(ipsuperviseur, port, "Preparateur/Charged",ippreparateur, 2)

			elif menu[current_row] == "Fin de Maintenance":
				ippreparateur="192.168.1.7"
				Robot.update_status(ippreparateur+"/1", "Occupied")
				publish(ipsuperviseur,port, "Preparateur/Prepare", ippreparateur+ "/1", 2)



#### Service ####


			elif menu[current_row] == "Service":
				menu = menu_service
				current_row = 0


			elif menu[current_row] == "Service/Go/Accueil":
				destination=Positions.get_Pose_by_name("accueil")[0][0]
				
				publish(ipsuperviseur, port, "Service/Go/Accueil", ip_choisie + "/" + str(destination), 2)


			elif menu[current_row] == "Service/Go/Table1":
				destination=Positions.get_Pose_by_name("table1")[0][0]
				publish(ipsuperviseur, port, "Service/Go/Table", ip_choisie + "/" + str(destination), 2)


			elif menu[current_row] == "Service/Go/Bar":
				destination=Positions.get_Pose_by_name("bar")[0][0]
				Robot.update_command("192.168.1.130/2",1)
				Robot.update_status(ip_choisie,"Occupied")
				Robot.update_command(ip_choisie,1)
				publish(ipsuperviseur, port, "Service/Go/Bar", ip_choisie + "/" + str(destination), 2)


			elif menu[current_row] == "Service/Go/Recharge":
				destination=Positions.get_Pose_by_name("recharge")[0][0]
				publish(ipsuperviseur, port, "Service/Go/Recharge", ip_choisie + "/" + str(destination), 2)


			elif menu[current_row] == "Service/Turn":
				publish(ipsuperviseur, port, "Service/Turn", ip_choisie, 2)
				



#### Return Trip ####


			elif menu[current_row] == "Return Trip":
				menu = menu_returntrip
				current_row = 0


			elif menu[current_row] == "ReturnTrip Table1":
				destination=Positions.get_Pose_by_name("table1")[0][0]
				publish(ipsuperviseur, port, "Service/ReturnTrip", ip_choisie + "/" + str(destination), 2)


			elif menu[current_row] == "ReturnTrip Table2":
				destination=Positions.get_Pose_by_name("table2")[0][0]
				publish(ipsuperviseur, port, "Service/ReturnTrip", ip_choisie + "/" + str(destination), 2)


			elif menu[current_row] == "ReturnTrip Table3":
				destination=Positions.get_Pose_by_name("table3")[0][0]
				publish(ipsuperviseur, port, "Service/ReturnTrip", ip_choisie + "/" + str(destination), 2)

			elif menu[current_row] == "ReturnTrip Recharge":
				destination=Positions.get_Pose_by_name("recharge")[0][0]
				publish(ipsuperviseur, port, "Service/ReturnTrip", ip_choisie + "/" + str(destination), 2)

#### Commande ####

			elif menu[current_row] == "Commande":
				menu = menu_commande
				current_row = 0

			elif menu[current_row] == "Nouvelle Commande":
				Commande.insert_Commande(1, 2, "Pending")
				Table.update_Table_status(2,"Pending")
				Table.update_Table_commandNbr(2, 1)
				publish(ipsuperviseur, port, "Commande/Envoi", "rien", 2)

			elif menu[current_row] == "Commande de plusieurs articles":		#Commande de une Jagger bombe + 2 verres d'eau pétillante
				Commande.insert_Commande(2, 1, "Pending")
				Commande.insert_Commande(2, 3, "Pending")
				Commande.insert_Commande(2, 3, "Pending")
				Table.update_Table_status(3,"Pending")
				Table.update_Table_commandNbr(3, 2)
					

			elif menu[current_row] == "Supprimer commande unique":
				Commande.delete_Commande(1)
				Table.update_Table_status(2,"Free")
				Table.update_Table_commandNbr(2, 0)
				publish(ipsuperviseur, port, "Commande/Envoi", "rien", 3)

			elif menu[current_row] == "Supprimer commande multiple":
				Commande.delete_Commande(2)
				Table.update_Table_status(3,"Free")
				Table.update_Table_commandNbr(3, 0)
				



#### Libérez ####
			elif menu[current_row] == "Libérez Robots":
				menu = menu_liberez_robots
				current_row = 0
			elif menu[current_row] == "Libérez Robotino":
				
				Robot.update_status("192.168.1.103", "Idle")
				Robot.update_command("192.168.1.103", 0)

			elif menu[current_row] == "Libérez TurtleBot":
				
				Robot.update_status("192.168.1.10", "Idle")
				Robot.update_command("192.168.1.10", 0)

			elif menu[current_row] == "Libérez Heron":
				
				Robot.update_status("192.168.1.3", "Idle")
				Robot.update_command("192.168.1.3", 0)

			elif menu[current_row] == "Libérez Mélangeur":
				
				Robot.update_status("192.168.1.7/1", "Idle")
				Robot.update_command("192.168.1.7/1", 0)

			elif menu[current_row] == "Libérez Manipulateur":
				
				Robot.update_status("192.168.1.130/2", "Idle")
				Robot.update_command("192.168.1.130/2", 0)

			elif menu[current_row] == "Free Dobby":
				listerobots=Robot.get_all_Robot()
				for i in listerobots:
					Robot.update_status(i[0], "Idle")
					Robot.update_command(i[0], 0)

			elif menu[current_row] == "CASSE TOI":
				Robot.update_status("192.168.1.10", "Occupied")




#### Autre ####


			elif menu[current_row] == "Back":
				menu = menu_accueil
				current_row = 0

			elif menu[current_row] == "Choix Robot":
				menu = menu_choix_robot
				current_row = 0

			elif menu[current_row] == "Robotino":
				titre_menu = "MENU ACCUEIL (Robotino / 192.168.1.103)"
				robot_choisi = "Robotino"
				ip_choisie = "192.168.1.103"
				menu = menu_accueil
				current_row = 0

			elif menu[current_row] == "Kobuki":
				titre_menu = "MENU ACCUEIL (Kobuki / 192.168.1.10)"
				robot_choisi = "Kobuki"
				ip_choisie = "192.168.1.10"
				menu = menu_accueil
				current_row = 0

			elif menu[current_row] == "Heron":
				titre_menu = "MENU ACCUEIL (Heron / 192.168.1.3)"
				robot_choisi = "Heron"
				ip_choisie = "192.168.1.3"
				menu = menu_accueil
				current_row = 0



		IHM.print_menu(stdscr, current_row, menu, titre_menu)
		
'''
			elif menu[current_row] == "Service/Go/Base":
				iprobot="192.168.1.103"
				destination=Positions.get_Pose_by_name("recharge")[0][0]
				publish(ipsuperviseur, port, "Service/Go/Base", iprobot+ "/" + str(destination), 2)
			'''		



######################
### Initialisation ###
######################


# Lancement IHM Initialisation

#subscribe(my_ip, port, "Initialisation/Envoi", 2)
#subscribe(my_ip, port, "Initialisation/Type", 2)

# Mode ecoute sur le topic de scan des nouveaux robots

# Si nouveau robot

	# Récupération des infos du message

	# Mise en BDD




############
### Main ###
############


# Lancement de L'IHM principale

curses.wrapper(main)


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
