# -*- coding: utf-8 -*-

############################################################
### Programme principal à lancer pour démarrer le projet ###
############################################################


###############
### Imports ###
###############

# Import des fichiers .py propre au projet

#import FonctionsMQTT
import mysql.connector
import IPFinder
import paho.mqtt.client as mqtt

# Import des librairies exterieures au projet

import time
import threading
import Positions
import rospy
import math

##########################
### Variables globales ###
##########################

#	Robot retrieves his own IP
my_ip=IPFinder.get_my_ip()

#	TCP port used for MQTT
port = 1883

desiredPose = []

#	Determines the supervisor's IP using the hosts file
hosts = open('/etc/hosts','r')
for line in hosts:
	try:
		if line.split()[1] == "supIP":
			ipsuperviseur = line.split()[0]
	except IndexError:
		pass

###	ROBOTS VARIABLES     ###
type_robot="Turtlebot"
etat_robot="libre"

######################
### Initialisation ###
######################


############
### Defs ###
############

f = "/home/nvidia/catkin2_ws/src/heron_isen/scripts/file/poses"

def loadFile():
	pose = dict()
	if os.path.isfile(f):
		if os.stat(f).st_size == 0:
			with open(f, 'wb') as fichier:
				pickler = pickle.Pickler(fichier)
				pickler.dump(pose)

		else:
			with open(f, 'rb') as fichier:
				depickler = pickle.Unpickler(fichier)
				pose = depickler.load()
				print(pose.keys())
				# print(pose.items())
	else:
		with open(f, 'wb'):
			pass
	return(pose)






def on_connect(client, userdata, flags, rc):

	print("Connected with result code "+str(rc))
	if rc==0:
		print("ok")
	else:
		print("no")


def on_disconnect(client, userdata, rc):

	print("Client Got Disconnected")


def on_message(client, userdata, msg):

	#print("Yes! i receive the message :" , str(msg.payload))
	#print("message received ", msg.payload.decode("utf-8"))
        #with open('data.json', 'w') as f:
        #json.dumps(msg.payload.decode("utf-8"))
	#print("message topic=",msg.topic)
	#print("message qos=",msg.qos)
	#print("message retain flag=",msg.retain)


	if (msg.topic=="Ordre/Envoi" and msg.payload.decode("utf-8").split("/")[0]==my_ip):
		global etat_robot
		etat_robot="occupe"
		print("ORDRE REçU")
		if (msg.payload.decode("utf-8").split("/")[1]=="Go"):

			# On cherche les coordonnées de la position donnée avec le fichier de pose sauvegardés

			pose = loadFile()
			desiredPose = position
			print(desiredPose)
			time.sleep(0.5)
			desiredPose = str(desiredPose)
			print(pose.get(desiredPose))



			# On cherche les coordonnées de la position donnée avec la bdd

			#position=msg.payload.decode("utf-8").split("/")[2]
			#print(position)
			#pose=Positions.get_Pose_by_name(mycursor,position)
			#print(pose)

			#global desiredPose
                        #desiredPose = pose[0]
                        #print(desiredPose)


			MoveToGoal()


	if (msg.topic=="Ping/Feedback" and msg.payload.decode("utf-8").split("/")[0]==my_ip):
		print("boucle feedback")
		if msg.payload.decode("utf-8").split("/")[1] == "No":
			print("boucle feedback no")
			publish(ipsuperviseur, port, "Initialisation/Envoi", my_ip+"/"+type_robot , 2)



#Appel d'une fonction qui permet de recevoir un message

def subscribe(ip, port, topic, qos):

	global client
	client = mqtt.Client()

	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.connect(ip,port,60)
	client.subscribe(topic, qos)
	client.loop_start()
	print("subscribed to "+topic)


#Appel d'une fonction qui permet d'envoyer un message

def publish(ip, port, topic, message, qos):

	client2 = mqtt.Client()

	client2.connect(ip,port,60)
	client2.loop_start()
	client2.publish(topic, message, qos)
	print("message sent on "+topic)


def pingRobot():

	threading.Timer(10, pingRobot).start()

	print ("Envoi du ping")

	publish(ipsuperviseur, 1883, "Robot/Ping", my_ip, 2)


def send_etat():
	publish(ipsuperviseur,1883,"Robot/Etat", my_ip+"/"+etat_robot,2)


def MoveToGoal():
	rospy.init_node('move_to_goal')
	# Create action client
	global client
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	rospy.loginfo("Waiting for move_base action server...")
	wait = client.wait_for_server(rospy.Duration(5.0))
	if not wait:
		rospy.logerr("Action server not available !")
		rospy.signal_shutdown("Action server not available !")
		return

	rospy.loginfo("Connected to move base server")
	rospy.loginfo("Start moving to " + str(desiredPose) + " ...")
	movebase_client()

def active_cb():
	rospy.loginfo("Goal pose " + str(desiredPose) + " is now being processed by the Action Server...")

def feedback_cb(feedback):
	rospy.loginfo("Feedback for goal pose " + str(desiredPose) + " received")


def done_cb(status, result):
	if status == 2:
		rospy.loginfo("Goal pose " + str(desiredPose) + " received a cancel request after it started executing, completed execution !")
	if status == 3:
		rospy.loginfo("Goal pose " + str(desiredPose) + " reached")
		return

	if status == 4:
		rospy.loginfo("Goal pose " + str(desiredPose) + " was aborted by the Action Server")

		rospy.signal_shutdown("Goal pose " + str(desiredPose)+" aborted, shutting down!")
		return

	if status == 5:
		rospy.loginfo("Goal pose " + str(desiredPose) + " has been rejected by the Action Server")

		rospy.signal_shutdown("Goal pose " + str(desiredPose) + " rejected, shutting down!")
		return

	if status == 8:
		rospy.loginfo("Goal pose " + str(desiredPose) + " received a cancel request before it started executing, successfully cancelled!")

def movebase_client():
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = "map"
	goal.target_pose.header.stamp = rospy.Time.now()
	goal.target_pose.pose.position.x = desiredPose[0]
	goal.target_pose.pose.position.y = desiredPose[1]
	goal.target_pose.pose.orientation.z = desiredPose[2]
	goal.target_pose.pose.orientation.w = desiredPose[3]
	rospy.loginfo("Sending goal pose " + str(desiredPose) + " to Action Server")
	rospy.loginfo(str(desiredPose))
	client.send_goal(goal, done_cb, active_cb, feedback_cb)
	#rospy.spin()
	return

###################################
###	PROGRAMME PRINCIPAL	###
###################################


###	CONNECTS TO DATABASE	###
flotte_db=mysql.connector.connect(
	host=ipsuperviseur,
	database='flotte_db',
	user='robot',
	password='robot'
)

global mycursor
mycursor=flotte_db.cursor()

pingRobot()

#	publish his IP and type separated by a / on Initialisation/Envoi
publish(ipsuperviseur, port, "Initialisation/Envoi", my_ip+"/"+type_robot , 2)

#	subscribe to Ordre/Envo - waits for orders
subscribe(ipsuperviseur, port, "Ordre/Envoi", 2)
subscribe(ipsuperviseur, port, "Ping/Feedback", 2)

while(1):
	time.sleep(10)






