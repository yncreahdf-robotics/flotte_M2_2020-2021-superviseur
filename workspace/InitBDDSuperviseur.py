import mysql.connector
import Article
import Commande
import Table
import Type
import Robot
import Positions


#	CREATE A NEW DATABASE
def create_flotte_db(mycursor):	
	mycursor.execute("CREATE DATABASE IF NOT EXISTS flotte_db")
	mycursor.execute("USE flotte_db")

#	Check if database exists
def check_flotte_db(mycursor):
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)

#	CREATE ALL TABLES
def create_all_tables(mycursor):
	Article.create_Article_tb(mycursor)
	Commande.create_Commande_tb(mycursor)
	Table.create_Table_tb(mycursor)
	Type.create_Type_tb(mycursor)
	Robot.create_Robot_tb(mycursor)
	Positions.create_Pose_tb(mycursor)

#	DELETE DATABASE
def delete_flotte_db(mycursor):
	sql="DROP DATABASE IF EXISTS flotte_db"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED **explosion**")


#	Initialisation

###	CONNECTS TO DATABASE	### 
flotte_db=mysql.connector.connect(
	host='localhost',
	database='flotte_db',
	user='root',
	password='L@boRobotique'
)

global mycursor
mycursor=flotte_db.cursor()


delete_flotte_db(mycursor)

create_flotte_db(mycursor)

create_all_tables(mycursor)

Positions.insert_Pose(flotte_db, "recharge", 0.2, 4.4, -0.1, -1)
Positions.insert_Pose(flotte_db, "table1", 2.4, 6.6, 0.96, 0.25)
Positions.insert_Pose(flotte_db, "table2", 1.15, 6.26, 0.76, -0.64)
Positions.insert_Pose(flotte_db, "table3", 1.86, 8.88, 0.27, -0.96)
Positions.insert_Pose(flotte_db, "bar", 4.5, 8.12, 0.95, -0.3)

Type.insert_Type(flotte_db, "Robotino", "Service", 20000)
Type.insert_Type(flotte_db, "Heron", "Service", 10000)
Type.insert_Type(flotte_db, "Turtlebot", "Service", 1000)
Type.insert_Type(flotte_db, "Caroita", "Preparateur", 500)
Type.insert_Type(flotte_db, "Accueil", "Accueil", -1)

