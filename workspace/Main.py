# -*- coding: utf-8 -*-

############################################################
### Programme principal à lancer pour démarrer le projet ###
############################################################




###############
### Imports ###
###############


# Import des fichiers .py propre au projet

import IHM


# Import des librairies exterieurs au projet

import curses




############
### Main ###
############


# Menus de l'interface

menu_accueil = ["Customer","Employee"]
menu_customer= ["Command","Call Waiter","Exit"]
menu_employee= ["Add New Robot","Follow Me","Start Service","Exit"]


# Boucle principale

def main(stdscr):
	
	menu = menu_accueil

	#turn off cursor blinking
	curses.curs_set(0)

	#color scheme for selected row
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	#specify the current selected row
	current_row = 0


	while 1:

		#print the menu
		IHM.print_menu(stdscr, current_row, menu)

		key = stdscr.getch()

		# Monte si la flèche du haut est pressée
		if key == curses.KEY_UP and current_row>0:
			current_row -= 1

		elif key == curses.KEY_DOWN and current_row < len(menu)-1:
			current_row +=1

		elif key == 27:
			break

		elif key in [10,13]:

			stdscr.clear()
			stdscr.refresh()

		# Menu Accueil
			if menu[current_row] == "Customer":
				menu = menu_customer
				current_row=0

			elif menu[current_row] == "Employee":
				menu = menu_employee
				current_row=0

		# Menu Customer
			elif menu[current_row] == "Command":
				#actions de commande
				pass

			elif menu[current_row] == "Call Waiter":
				#appel de serveur humain
				pass

		# Menu Employee
			elif menu[current_row] == "Add New Robot":
				#ajout de robot à la flotte
				pass

			elif menu[current_row] == "Follow Me":
				#mode suivi de personne
				pass

			elif menu[current_row] == "Start Service":
				#démarrage fonctions robot
				pass

		# Commun Menus
			elif menu[current_row] == "Exit":
				menu = menu_accueil
				current_row=0



# Lancement de l'interface homme machine
curses.wrapper(main)


