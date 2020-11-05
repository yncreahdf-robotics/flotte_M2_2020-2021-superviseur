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



# Import des librairies exterieures au projet

import curses
import time
import paho.mqtt.client as mqtt



##########################
### Variables globales ###
##########################


port = 1883

menu_accueil = ["Bienvenue"]

ipsuperviseur = ""




############
### Defs ###
############



def on_connect(client, userdata, flags, rc):

	#print("Connected with result code "+str(rc))
	if rc==0:
		#print("connection ok")
		pass
	else:
		#print("connection no")
		pass

	


def on_disconnect(client, userdata, rc):

	print("Client Got Disconnected")


def on_message(client, userdata, msg):

	#print("Yes! i receive the message :" , str(msg.payload))
	#print("message received ", msg.payload.decode("utf-8"))
	#print("message topic=",msg.topic)
	#print("message qos=",msg.qos)
	#print("message retain flag=",msg.retain)

	if msg.topic == "Initialisation/Envoi":

		global menu_accueil

		if not msg.payload.decode("utf-8") in menu_accueil:

			menu_accueil.append(msg.payload.decode("utf-8"))

		AvailableIP = IPFinder.launch

		for ip in AvailableIP():

			try:
				publish(ip, 1883, "Initialisation/Feedback", str(IPFinder.get_my_ip()), 2)

			except OSError as err:

				pass



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





def main(stdscr):
	
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

		elif key == curses.KEY_DOWN and current_row < len(menu)-1:
			current_row +=1

		elif key == 27:
			break

		elif key in [10,13]:
			stdscr.clear()
			stdscr.refresh()

			#Pour chaque appui sur un choix on lance la publication d'un msg à l'aide du python mqttperso.py
			if menu[current_row] == "Test":

				AvailableIP = IPFinder.launch

				for i in AvailableIP():
					
					try:
						publish(i, port, "Initialisation/Feedback", IPFinder.get_my_ip(), 2)
						print(i)
					except OSError as err:
						print("OS error: {0}".format(err))
					

			#elif menu[current_row] == "Demonstration navigation (initialisation)":
			#	mqttperso.publish(ip, port, "topic/Ordre", "1", 0)
		
		IHM.print_menu(stdscr, current_row, menu)

		print(ipsuperviseur)

		




######################
### Initialisation ###
######################


# Lancement IHM Initialisation

subscribe(IPFinder.get_my_ip(), port, "Initialisation/Envoi", 2)

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
