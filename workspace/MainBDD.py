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

create_all_tables(mycursor)

#############################
#####	CODE ROBOT	#####
#####	READ ONLY	#####
#############################
# exemple Article.get_all_articles(mycursor)

