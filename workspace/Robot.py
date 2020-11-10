import mysql.connector
from datetime import datetime

#	CREATE A NEW DATABASE
def create_flotte_db():	
	mycursor=flotte_db.cursor()
	mycursor.execute("CREATE DATABASE IF NOT EXISTS flotte_db")
	mycursor.execute("USE flotte_db")

#	Check if database exists
def check_flotte_db():
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)

#	CREATE A NEW TABLE
def create_Robot_tb():
	mycursor.execute("CREATE TABLE IF NOT EXISTS Robot_tb (RobotID INT AUTO_INCREMENT, RobotType VARCHAR(30), Position VARCHAR(30), Etat VARCHAR(30), LastCheck DATETIME, CONSTRAINT RobotID_pk PRIMARY KEY (RobotID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Robot_tb():	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT RobotS IN THE COMMAND DATABASE
def insert_Robot(RobotType, Position, Etat, LastCheck):
	#need to verify that the RobotType is an existing Type in the  Type database
	sql="INSERT INTO Robot_tb (RobotType, Position, Etat, LastCheck) VALUES(%s,%s,%s,%s)"
	val=(RobotType, Position, Etat, LastCheck)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Robot ajouté")

#	GET ALL POSSIBLE RobotS
def get_all_Robot():
	sql="SELECT * FROM Robot_tb ORDER BY RobotType"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET A Robot BY ITS NAME
def get_Robot_by_name(RobotType):
	sql = "SELECT * FROM Robot_tb WHERE RobotName=RobotName IF EXISTS"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A Robot
def delete_Robot(RobotID):
	sql="DELETE FROM Robot_tb WHERE RobotID=RobotID"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Robot deleted")

def delete_flotte_db():
	sql="DROP DATABASE flotte_db"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED **explosion**")

if __name__ == '__main__':

	#initialisation 
	flotte_db=mysql.connector.connect(
		host='localhost',
		user='root',
		password='password'
		)
	mycursor=flotte_db.cursor()

	create_flotte_db()
	check_flotte_db()

	create_Robot_tb()
	check_Robot_tb()


	insert_Robot('Service', 'ServiceBase1', "Libre", datetime.now() )
	insert_Robot('Service','Bar', "Occupe", datetime.now())
	insert_Robot('Service','table 1', "Occupe", datetime.now())
	insert_Robot('Preparateur', 'PrepaBar', "Occupe", datetime.now())
	insert_Robot('Accueil', 'Accueil', "Libre", datetime.now())
	get_all_Robot();
	delete_flotte_db()
