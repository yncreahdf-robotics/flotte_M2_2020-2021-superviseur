# -*- coding: utf-8 -*-


'''import roslaunch
import rospy'''
import curses
import subprocess
import os
import time



menu_accueil = ["Customer","Employee"]
menu_customer= ["Command","Call Waiter","Exit"]
menu_employee= ["Add New Robot","Follow Me","Start Service","Exit"]


def print_menu(stdscr, selected_row_idx, menu):
	stdscr.clear()
	h,w=stdscr.getmaxyx() 	#	get the size of the screen height and width
	stdscr.addstr(h//2-len(menu)//2, w//2 - len("MENU FLOTTE")//2,"MENU FLOTTE")
	#consigne = "Use ARROWS to navigate and ENTER to validate - ESC to leave:"
	for idx,row in enumerate(menu):
		x=w//2-len(row)//2
		y=h//2+((idx+2)*2)-len(menu)//2
		if idx == selected_row_idx:	#	Whiten the selected option
			stdscr.attron(curses.color_pair(1))	#	turn on the attribute of color
			stdscr.addstr(y,x,row)	#	print the selected row on x,y
			stdscr.attroff(curses.color_pair(1))	#	turn off the attribute of color
		else:
			stdscr.addstr(y,x,row)
	stdscr.refresh()	#	Affiche les derniers changements apportés


#Prints text centered
def print_center(stdscr,text):
	stdscr.clear()
	h,w = stdscr.getmaxyx()
	x=w//2 - len(text)//2
	y=h//2
	stdscr.addstr(y,x,text)
	stdscr.refresh()


def main(stdscr):
	
	menu=menu_accueil

	#turn off cursor blinking
	curses.curs_set(0)

	#color scheme for selected row
	curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)

	#specify the current selected row
	current_row = 0

	#print the menu
	print_menu(stdscr, current_row, menu)
	

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
			if menu[current_row] == "Customer":
				menu=menu_customer
				current_row=0
			elif menu[current_row] == "Employee":
				menu=menu_employee
				current_row=0
			elif menu[current_row] == "Command":
				#actions de commande
				pass
			elif menu[current_row] == "Call Waiter":
				#appel de serveur humain
				pass
			elif menu[current_row] == "Add New Robot":
				#ajout de robot à la flotte
				pass
			elif menu[current_row] == "Follow Me":
				#mode suivi de personne
				pass
			elif menu[current_row] == "Start Service":
				#démarrage fonctions robot
				pass
			elif menu[current_row] == "Exit":
				menu=menu_accueil
				current_row=0
		
		print_menu(stdscr, current_row, menu)

curses.wrapper(main)

