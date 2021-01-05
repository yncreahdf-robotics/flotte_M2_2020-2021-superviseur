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


menu_accueil = ["Preparateur", "Service", "Commande", "Free Dobby", "Return Trip", "CASSE TOI"]
menu_preparateur = ["Preparateur/Prepare", "Preparateur/Charge", "Back"]
menu_service = ["Service/Go/Bar", "Service/Go/Table", "Service/Turn", "Service/Nassima", "Back"]
menu_returntrip = ["ReturnTrip Table1", "ReturnTrip Table2", "ReturnTrip Table3", "Back"]



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

	#turn off cursor blinking
	curses.curs_set(0)

	#color scheme for selected row
	curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)

	#specify the current selected row
	current_row = 0

	#print the menu
	IHM.print_menu(stdscr, current_row, menu)
	

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

			#Pour chaque appui sur un choix on lance la publication d'un msg à l'aide du python mqttperso.py
			if menu[current_row] == "Preparateur/Prepare":
				ippreparateur="192.168.1.8"
				Commande.update_status(1, "Ordered")
				publish(ipsuperviseur, port, "Preparateur/Prepare",ippreparateur + "/1", 2)


			elif menu[current_row] == "Preparateur/Charge":
				ippreparateur="192.168.1.8"
				publish(ipsuperviseur, port, "Preparateur/Charge",ippreparateur + "/1", 2)

			elif menu[current_row] == "Service/Go/Bar":
				iprobot="192.168.1.11"
				destination=Positions.get_Pose_by_name("bar")[0][0]
				publish(ipsuperviseur, port, "Service/Go/Bar", iprobot + "/" + str(destination), 2)

			elif menu[current_row] == "Service/Go/Table":
				iprobot="192.168.1.103"
				destination=Positions.get_Pose_by_name("table2")[0][0]
				publish(ipsuperviseur, port, "Service/Go/Table", iprobot + "/" + str(destination), 2)

			elif menu[current_row] == "Service/Nassima":
				iprobot="192.168.1.10"
				destination=Positions.get_Pose_by_name("recharge")
				publish(ipsuperviseur, port, "Service/ReturnTrip", iprobot + "/" + str(destination[0][0]), 2)

			elif menu[current_row] == "Service/Turn":
				iprobot="192.168.1.103"
				publish(ipsuperviseur, port, "Service/Turn", iprobot, 2)
				
			elif menu[current_row] == "Commande":
				Commande.insert_Commande(1, 1, "Pending")
				publish(ipsuperviseur, port, "Commande/Envoi", "rien", 2)
				Table.update_Table_commandNbr(2, 1)
				CommandNbr+=1
				
			elif menu[current_row] == "Free Dobby":
				listerobots=Robot.get_all_Robot()
				for i in listerobots:
					Robot.update_status(i[0], "Idle")


			elif menu[current_row] == "Return Trip":
				menu = menu_returntrip
				current_row = 0


			elif menu[current_row] == "Preparateur":
				menu = menu_preparateur
				current_row = 0


			elif menu[current_row] == "Service":
				menu = menu_service
				current_row = 0

			elif menu[current_row] == "Back":
				menu = menu_accueil
				current_row = 0

			elif menu[current_row] == "ReturnTrip Table1":
				publish(ipsuperviseur, port, "Service/ReturnTrip", "table1", 2)

			elif menu[current_row] == "ReturnTrip Table2":
				publish(ipsuperviseur, port, "Service/ReturnTrip", "table2", 2)

			elif menu[current_row] == "ReturnTrip Table3":
				publish(ipsuperviseur, port, "Service/ReturnTrip", "table3", 2)

			elif menu[current_row] == "CASSE TOI":
				Robot.update_status("192.168.1.10", "Occupied")



		IHM.print_menu(stdscr, current_row, menu)
		
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
