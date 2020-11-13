import mysql.connector
from datetime import datetime



#	CREATE A NEW TABLE
def create_Pose_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS Pose_tb (PoseID INT AUTO_INCREMENT, PoseName VARCHAR(30), PoseX FLOAT, PoseY FLOAT, PoseW FLOAT, PoseZ FLOAT, CONSTRAINT PoseID_pk PRIMARY KEY (PoseID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Pose_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT POSES IN THE COMMAND DATABASE
def insert_Pose(mycursor, PoseName, PoseX, PoseY, PoseW, PoseZ):
	sql="INSERT INTO Pose_tb (PoseName, PoseX, PoseY, PoseW, PoseZ) VALUES(%s,%s,%s,%s,%s)"
	val=(PoseName, PoseX, PoseY, PoseW, PoseZ)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Pose ajoutée")

#	GET ALL POSSIBLE PoseS
def get_all_Pose(mycursor):
	sql="SELECT * FROM Pose_tb ORDER BY PoseName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET A Pose BY ITS NAME
def get_Pose_by_name(mycursor, PoseName):
	sql = "SELECT * FROM Pose_tb WHERE PoseName=PoseName IF EXISTS"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A Pose
def delete_Pose(mycursor, PoseName):
	sql="DELETE FROM Pose_tb WHERE PoseName=" + PoseName
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Pose deleted")



