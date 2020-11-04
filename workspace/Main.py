# -*- coding: utf-8 -*-

############################################################
### Programme principal à lancer pour démarrer le projet ###
############################################################




###############
### Imports ###
###############


# Import des fichiers .py propre au projet

import IHM
import FonctionsMQTT
import IPFinder


# Import des librairies exterieures au projet

import curses
import time



##########################
### Variables globales ###
##########################


ip = "192.168.1.5"
port = 1883

menu_accueil = ["Test"]




######################
### Initialisation ###
######################


# Lancement IHM Initialisation

# Mode ecoute sur le topic de scan des nouveaux robots

# Si nouveau robot

	# Récupération des infos du message

	# Mise en BDD




############
### Defs ###
############



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
						FonctionsMQTT.publish(i, port, "topiCoco", "testmessage", 0)
						print(i)
					except OSError as err:
						print("OS error: {0}".format(err))
					
				#mqttperso.publish(ip, port, "topiCoco", "testmessage", 0)

			#elif menu[current_row] == "Demonstration navigation (initialisation)":
			#	mqttperso.publish(ip, port, "topic/Ordre", "1", 0)
		
		IHM.print_menu(stdscr, current_row, menu)

		




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
