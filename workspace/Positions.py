import mysql.connector
from datetime import datetime


#########################################
##	Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Pose_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS Pose_tb (PoseID INT AUTO_INCREMENT, PoseName VARCHAR(30), PoseX FLOAT, PoseY FLOAT, PoseZ FLOAT, PoseW FLOAT, CONSTRAINT PoseID_pk PRIMARY KEY (PoseID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Pose_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)


############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT POSES IN THE COMMAND DATABASE
def insert_Pose(flotte_db, PoseName, PoseX, PoseY, PoseZ, PoseW):
	sql="INSERT INTO Pose_tb (PoseName, PoseX, PoseY, PoseZ, PoseW) VALUES(%s,%s,%s,%s,%s)"
	val=(PoseName, PoseX, PoseY, PoseZ, PoseW)
	mycursor=flotte_db.cursor()
	mycursor.execute(sql,val)
	flotte_db.commit()
	print("BDD:     ", mycursor.rowcount,"Pose ajoutée")


###################################
##  Fonctions d'accès a la table ##
###################################

#	GET ALL POSSIBLE POSES
def get_all_Pose(mycursor):
	sql="SELECT * FROM Pose_tb ORDER BY PoseName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)

#	GET A POSE BY ITS NAME
def get_Pose_by_name(mycursor, PoseName):
	sql = "SELECT PoseID FROM Pose_tb WHERE PoseName=\"" + PoseName + "\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult


###############################
##  Fonction de suppression  ##
###############################

#	DELETE A Pose
def delete_Pose(flotte_db, PoseName):
	sql="DELETE FROM Pose_tb WHERE PoseName=" + PoseName
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print("BDD:		", mycursor.rowcount,"Pose deleted")



