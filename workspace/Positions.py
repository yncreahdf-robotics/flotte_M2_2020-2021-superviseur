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
def create_Pose_tb():
	mycursor.execute("CREATE TABLE IF NOT EXISTS Pose_tb (PoseID INT AUTO_INCREMENT, PoseName VARCHAR(30), PoseX FLOAT, PoseY FLOAT, PoseW FLOAT, PoseZ FLOAT, CONSTRAINT PoseID_pk PRIMARY KEY (PoseID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Pose_tb():	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT POSES IN THE COMMAND DATABASE
def insert_Pose(PoseName, PoseX, PoseY, PoseW, PoseZ):
	#need to verify that the PoseType is an existing Type in the  Type database
	sql="INSERT INTO Pose_tb (PoseName, PoseX, PoseY, PoseW, PoseZ) VALUES(%s,%s,%s,%s,%s)"
	val=(PoseName, PoseX, PoseY, PoseW, PoseZ)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Pose ajoutée")

#	GET ALL POSSIBLE PoseS
def get_all_Pose():
	sql="SELECT * FROM Pose_tb ORDER BY PoseName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET A Pose BY ITS NAME
def get_Pose_by_name(PoseName):
	sql = "SELECT * FROM Pose_tb WHERE PoseName=PoseName IF EXISTS"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A Pose
def delete_Pose(PoseName):
	sql="DELETE FROM Pose_tb WHERE PoseName=PoseName"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Pose deleted")

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

	create_Pose_tb()
	check_Pose_tb()


	insert_Pose('Bar', 12.4 , 115.3, 10.1, 666)
	insert_Pose('ServiceBase1', 38.4 , 49.0, 399, 32.3)
	insert_Pose('ServiceBase2', 38.4 , 67.0, 399, 32.3)
	insert_Pose('Table1', 183 , 139, 30, 33)
	insert_Pose('Table2', 13 , 13, 3, 3)
	get_all_Pose();
	delete_flotte_db()
