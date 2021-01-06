# -*- coding: utf-8 -*-


import curses


def print_menu(stdscr, selected_row_idx, menu, titre):
	stdscr.clear()
	h,w=stdscr.getmaxyx() 	#	get the size of the screen height and width
	stdscr.addstr(h//2-len(menu)//2, w//2 - len(titre)//2,titre)
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

