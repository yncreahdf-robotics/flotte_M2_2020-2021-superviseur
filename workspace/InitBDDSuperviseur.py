import Article
import Commande
import Table
import Type
import Robot
import Positions


#	CREATE A NEW DATABASE
def create_flotte_db(flotte_db):
	mycursor=flotte_db.cursor()	
	mycursor.execute("CREATE DATABASE IF NOT EXISTS flotte_db")
	mycursor.execute("USE flotte_db")

#	Check if database exists
def check_flotte_db(mycursor):
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)

#	CREATE ALL TABLES
def create_all_tables(flotte_db):
	mycursor=flotte_db.cursor()
	Article.create_Article_tb(mycursor)
	Commande.create_Commande_tb(mycursor)
	Table.create_Table_tb(mycursor)
	Type.create_Type_tb(mycursor)
	Robot.create_Robot_tb(mycursor)
	Positions.create_Pose_tb(mycursor)

#	DELETE DATABASE
def delete_flotte_db(flotte_db):
	sql="DROP DATABASE IF EXISTS flotte_db"
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED **explosion**")
