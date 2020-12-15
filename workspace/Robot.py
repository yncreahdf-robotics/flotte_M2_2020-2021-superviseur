import mysql.connector
from datetime import datetime

#########################################
##	Fonctions de Création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Robot_tb(flotte_db):
	try:
		mycursor=flotte_db.cursor()
		mycursor.execute("CREATE TABLE IF NOT EXISTS Robot_tb (RobotIP VARCHAR(30) NOT NULL PRIMARY KEY, RobotType VARCHAR(30), Position INT, Etat VARCHAR(30), ActiveCommandNbr INT, LastCheck DATETIME)" ) 
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Robot_tb(flotte_db):	
	try:
		mycursor=flotte_db.cursor()
		mycursor.execute("SHOW TABLES")
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

###########################################
##	Fonctions de remplissage de la table ##
###########################################

#	INSERT RobotS IN THE COMMAND DATABASE
def insert_Robot(flotte_db, RobotIP, RobotType, Position, Etat, ActiveCommandNbr, LastCheck):
	try:
		#need to verify that the RobotType is an existing Type in the  Type database
		sql="INSERT INTO Robot_tb (RobotIP, RobotType, Position, Etat, ActiveCommandNbr, LastCheck) VALUES(%s,%s,%s,%s,%s,%s)"
		val=(RobotIP, RobotType, Position, Etat, ActiveCommandNbr, LastCheck)
		mycursor=flotte_db.cursor()
		mycursor.execute(sql,val)
		flotte_db.commit()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

####################################
##	Fonctions d'accès à la table  ##
####################################

#	GET ALL ROBOTS
def get_all_Robot(flotte_db):
	try:
		sql="SELECT * FROM Robot_tb ORDER BY RobotType"
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		mycursor.close()
		return myresult 	
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET A LIST OF ROBOTS BY ROLE
def find_robot_by_role(flotte_db,role):
	try:
		sql = "SELECT RobotIP FROM Robot_tb INNER JOIN Type_tb ON Robot_tb.RobotType=Type_tb.TypeName WHERE Type_tb.Role= \""+ role+"\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET A LIST OF ROBOT BY ROLE AND STATUS
def find_robot_by_role_and_status(flotte_db, role, status):
	try:
		sql="SELECT RobotIP FROM Robot_tb INNER JOIN Type_tb ON Robot_tb.RobotType=Type_tb.TypeName WHERE Type_tb.Role = \""+ role + "\" AND Etat = \"" + status + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#GET A ROBOT BY ITS ROLE AND STATUS TO A CERTAIN POSITION
def find_robot_by_role_status_and_position(flotte_db, role, position, status):
	try:
		sql="SELECT RobotIP FROM Robot_tb INNER JOIN Type_tb ON Robot_tb.RobotType=Type_tb.TypeName WHERE Type_tb.Role= \""+ role+ "\" AND Etat = \"" + status + "\" AND Position = \"" + position + "\""
		mycursor=flotte_db.cursor()	
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult 
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#GET A ROBOTS DATA BY ITS IP
def get_robot_data(flotte_db, RobotIP):
	try:
		sql="SELECT * FROM Robot_tb WHERE RobotIP=\""+ RobotIP + "\""
		mycursor=flotte_db.cursor()	
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET A ROBOT BY ITS ACTIVE COMMAND NUMBER
def get_robot_by_ActiveCommand(flotte_db,ActiveCommandNbr):
	
	try:
		sql= "SELECT RobotIP FROM Robot_tb WHERE ActiveCommandNbr= \"" + ActiveCommandNbr + "\""
		mycursor=flotte_db.cursor()	
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

############################################
##	Fonctions de mise à jour de la table  ##
############################################

# UPDATE A ROBOT STATUS
def update_status(flotte_db, RobotIP, newStatus):
	try:
		sql = "UPDATE Robot_tb SET Etat = \"" + newStatus + "\" WHERE RobotIP = \"" + str(RobotIP) + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	UPDATE A ROBOT'S LAST POSITION
def update_position(flotte_db, RobotIP, newPosition):
	try:
		sql = "UPDATE Robot_tb SET Position = \"" + newPosition + "\" WHERE RobotIP = \"" + str(RobotIP) + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	UPDATE LAST CHECK OF ROBOT
def update_ping(flotte_db, RobotIP):
	try:
		sql = "UPDATE Robot_tb SET LastCheck = \"" + str(datetime.now()) + "\" WHERE RobotIP = \"" + RobotIP + "\""
		val=datetime.now()
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	UPDATE THE COMMAND THE ROBOT IS WORKING ON
def update_command(flotte_db,RobotIP, newCommandNbr):
	try:
		sql = "UPDATE Robot_tb SET ActiveCommandNbr= \"" + str(newCommandNbr) + "\" WHERE RobotIP = \"" + RobotIP + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#########################################################
##	Fonctions de suppression d'éléments dans la table  ##
#########################################################

#	DELETE A Robot 
def delete_Robot(flotte_db, RobotIP):
	try:
		sql="DELETE FROM Robot_tb WHERE RobotIP=\""+RobotIP+"\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

