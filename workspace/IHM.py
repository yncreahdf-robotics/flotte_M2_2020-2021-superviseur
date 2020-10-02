# -*- coding: utf-8 -*-


'''import roslaunch
import rospy'''
import curses
import subprocess
import os
import time


"""
#Fonction to modify the IP at lines ROS_MASTER_URI et ROS_HOSTNAME du .zshrc
def modifIP(stdscr):
    stdscr.clear()	#clear the screen
    curses.echo()  #prints what's typed on the keyboard
    stdscr.addstr("Adresse IP Superviseur ? (Enter to continue, NO SPACES)\nExample : 10.224.0.52\n")
    ip_sup = stdscr.getstr() #Retrieves supervisor's IP
    stdscr.clear()	#clear screen
    stdscr.addstr("Adresse IP Robot ? (Enter to continue, NO SPACES)\nExample : 10.224.0.51\n")
    ip_robot = stdscr.getstr() #Retrieves Robot's IP
    curses.noecho() #unables character printing on the screen

    file = open("/home/nvidia/.zshrc", "r")	# "r"=reading 
    content=file.readlines()
    file.close()
    for i in range(len(content)):
        if ("ROS_MASTER") in content[i]:
            content[i] = "export ROS_MASTER_URI=http://"+ip_sup+":11311"
        if ("ROS_HOSTNAME") in content[i]:
            content[i] = "\nexport ROS_HOSTNAME="+ip_robot+"\n"

    file2 = open("/home/nvidia/.zshrc", "w")
    for line in content:
        file2.write(line)
    file2.close()
    """

def modifIP_sup(stdscr):
	stdscr.clear()	#	clear the screen
	curses.echo() 	#	enable to print what's typed on keyboard
	stdscr.addstr("Enter the supervisors IP \n (No spaces allowed) \n Press Enter to continue")	#	print to the screen
	ip_sup=stdscr.getstr()	#	Retrieves supervisor's IP
	file=open("/path","r")		#	Open the file at the given path
	content=file.readlines()	#	Reads file until its end
	for i in range(len(content)):
		if("ROS_MASTER") in content [i]:
			content [i] = "export ROS_MASTER_URI=http://"+ip_supp+":11311"
	file2 = open("/path","r")
	for line in content:
		file2.write(line)
	file2.close()

def modifIP_robot(stdscr):
	stdscr.clear()	#	clear the screen
	curses.echo() 	#	enable to print what's typed on keyboard
	stdscr.addstr("Enter the robot /add id/ IP \n (No spaces allowed) \n Press Enter to continue")	#	print to the screen
	ip_robot=stdscr.getstr()	#	Retrieves supervisor's IP
	file=open("/path","r")		#	Open the file at the given path
	content=file.readlines()	#	Reads file until its end
	for i in range(len(content)):
		if("ROS_HOSTNAME") in content [i]:	#	!!! need to add an id verification to modify only the ID of the right robot
			content [i] = "export ROS_MASTER_URI=http://"+ip_supp+":11311"
	file2 = open("/path","r")
	for line in content:
		file2.write(line)
	file2.close()

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


#changes the environment variables for  ROS_MASTER_URI and ROS_HOSTNAME
'''def set_environment(master, ip):
	os.environ['ROS_MASTER_URI']=master
	os.environ['ROS_HOSTNAME']=ip

#Retrieves the environment variables for ROS_MASTER_URI and ROS_HOSTNAME
def get_environment():
	return os.environ['ROS_MASTER_URI'], os.environ['ROS_HOSTNAME']
'''
#Prints text centered
def print_center(stdscr,text):
	stdscr.clear()
	h,w = stdscr.getmaxyx()
	x=w//2 - len(text)//2
	y=h//2
	stdscr.addstr(y,x,text)
	stdscr.refresh()

#Launches
'''def start_launch(launch_name,stdscr):
	stdscr.nodelay(1)
	uuid=roslaunch.rlutil.get_or_generate_uuid(None,True)
	roslaunch.configure_logging(uuid)
	launch=roslaunch.parent.ROSLaunchParent(uuid,['path'])
	launch.start()	#start ros launch
	while stdscr.getch() != 27: # 27=ESC
		pass
	launch.shutdown()	#	ends launch
'''
