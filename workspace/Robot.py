import mysql.connector
from datetime import datetime

#########################################
##	Fonctions de Création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Robot_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS Robot_tb (RobotIP VARCHAR(30) NOT NULL PRIMARY KEY, RobotType VARCHAR(30), Position VARCHAR(30), Etat VARCHAR(30), ActiveCommandNbr INT, LastCheck DATETIME)" ) 

#	CHECK IF THE TABLE EXISTS
def check_Robot_tb(mycursor):	
	mycursor.execute("SHOW TABLES")

###########################################
##	Fonctions de remplissage de la table ##
###########################################

#	INSERT RobotS IN THE COMMAND DATABASE
def insert_Robot(flotte_db, RobotIP, RobotType, Position, Etat, ActiveCommandNbr, LastCheck):
	#need to verify that the RobotType is an existing Type in the  Type database
	sql="INSERT INTO Robot_tb (RobotIP, RobotType, Position, Etat, ActiveCommandNbr, LastCheck) VALUES(%s,%s,%s,%s,%s,%s)"
	val=(RobotIP, RobotType, Position, Etat, ActiveCommandNbr, LastCheck)
	mycursor=flotte_db.cursor()
	mycursor.execute(sql,val)
	flotte_db.commit()

####################################
##	Fonctions d'accès à la table  ##
####################################

#	GET ALL ROBOTS
def get_all_Robot(mycursor):
	sql="SELECT * FROM Robot_tb ORDER BY RobotType"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	return myresult 

#	GET A LIST OF ROBOTS BY ROLE
def find_robot_by_role(mycursor,role):
	sql = "SELECT RobotIP FROM Robot_tb INNER JOIN Type_tb ON Robot_tb.RobotType=Type_tb.TypeName WHERE Type_tb.Role= \""+ role+"\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult

#	GET A LIST OF ROBOT BY ROLE AND STATUS
def find_robot_by_role_and_status(mycursor, role, status):
	sql="SELECT RobotIP FROM Robot_tb INNER JOIN Type_tb ON Robot_tb.RobotType=Type_tb.TypeName WHERE Type_tb.Role = \""+ role + "\" AND Etat = \"" + status + "\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult

#GET A ROBOT BY ITS ROLE AND STATUS TO A CERTAIN POSITION
def find_robot_by_role_status_and_position(mycursor, role, position, status):
	sql="SELECT RobotIP FROM Robot_tb INNER JOIN Type_tb ON Robot_tb.RobotType=Type_tb.TypeName WHERE Type_tb.Role= \""+ role+ "\" AND Etat = \"" + status + "\" AND Position = \"" + position + "\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult 

#GET A ROBOTS DATA BY ITS IP
def get_robot_data(mycursor, RobotIP):
	sql="SELECT * FROM Robot_tb WHERE RobotIP=\""+ RobotIP + "\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult

#	GET A ROBOT BY ITS ACTIVE COMMAND NUMBER
def get_robot_by_ActiveCommand(mycursor,ActiveCommandNbr):
	sql= "SELECT RobotIP FROM Robot_tb WHERE ActiveCommandNbr= \"" + ActiveCommandNbr + "\""
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	return myresult


############################################
##	Fonctions de mise à jour de la table  ##
############################################

# UPDATE A ROBOT STATUS
def update_status(flotte_db, RobotIP, newStatus):
	sql = "UPDATE Robot_tb SET Etat = \"" + newStatus + "\" WHERE RobotIP = \"" + str(RobotIP) + "\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	
#	UPDATE A ROBOT'S LAST POSITION
def update_position(flotte_db, RobotIP, newPosition):
	sql = "UPDATE Robot_tb SET Position = \"" + newPosition + "\" WHERE RobotIP = \"" + str(RobotIP) + "\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()

#	UPDATE LAST CHECK OF ROBOT
def update_ping(flotte_db, RobotIP):
	sql = "UPDATE Robot_tb SET LastCheck = \"" + str(datetime.now()) + "\" WHERE RobotIP = \"" + RobotIP + "\""
	val=datetime.now()
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()

#	UPDATE THE COMMAND THE ROBOT IS WORKING ON
def update_command(flotte_db,RobotIP, newCommandNbr):
	sql = "UPDATE Robot_tb SET ActiveCommandNbr= \"" + str(newCommandNbr) + "\" WHERE RobotIP = \"" + RobotIP + "\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()

#########################################################
##	Fonctions de suppression d'éléments dans la table  ##
#########################################################

#	DELETE A Robot 
def delete_Robot(flotte_db, RobotIP):
	sql="DELETE FROM Robot_tb WHERE RobotIP=\""+RobotIP+"\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()


