import mysql.connector
from datetime import datetime



#	CREATE A NEW TABLE
def create_Robot_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS Robot_tb (RobotID INT AUTO_INCREMENT, RobotType VARCHAR(30), Position VARCHAR(30), Etat VARCHAR(30), LastCheck DATETIME, CONSTRAINT RobotID_pk PRIMARY KEY (RobotID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Robot_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT RobotS IN THE COMMAND DATABASE
def insert_Robot(mycursor, RobotType, Position, Etat, LastCheck):
	#need to verify that the RobotType is an existing Type in the  Type database
	sql="INSERT INTO Robot_tb (RobotType, Position, Etat, LastCheck) VALUES(%s,%s,%s,%s)"
	val=(RobotType, Position, Etat, LastCheck)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Robot ajouté")

#	GET ALL POSSIBLE RobotS
def get_all_Robot(mycursor):
	sql="SELECT * FROM Robot_tb ORDER BY RobotType"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET A Robot BY ITS NAME
def get_Robot_by_name(mycursor, RobotType):
	sql = "SELECT * FROM Robot_tb WHERE RobotName="+RobotName+" IF EXISTS"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A Robot
def delete_Robot(mycursor, RobotID):
	sql="DELETE FROM Robot_tb WHERE RobotID="+RobotID
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Robot deleted")


