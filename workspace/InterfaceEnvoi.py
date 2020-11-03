# -*- coding: utf-8 -*-

############################################################
### Programme principal à lancer pour démarrer le projet ###
############################################################




###############
### Imports ###
###############


# Import des fichiers .py propre au projet

import IHM
import mqttperso


# Import des librairies exterieures au projet

import curses



##########################
### Variables globales ###
##########################


ip = "192.168.1.3"

menu_accueil = ["Initialisation", "bouton2"]
#menu_customer= ["Command","Call Waiter","Exit"]
#menu_employee= ["Add New Robot","Follow Me","Start Service","Exit"]




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
			if menu[current_row] == "Initialisation":
				mqttperso.publish(ip, 1883, "topiCoco", "testmessage", 2)
			elif menu[current_row] == "bouton2":
				pass
		
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
