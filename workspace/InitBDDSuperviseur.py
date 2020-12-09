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
	mycursor.close()

#	Check if database exists
def check_flotte_db(flotte_db):
	mycursor=flotte_db.cursor()
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)
	mycursor.close()

#	CREATE ALL TABLES
def create_all_tables(flotte_db):
	mycursor=flotte_db.cursor()
	Article.create_Article_tb(flotte_db)
	Commande.create_Commande_tb(flotte_db)
	Table.create_Table_tb(flotte_db)
	Type.create_Type_tb(flotte_db)
	Robot.create_Robot_tb(flotte_db)
	Positions.create_Pose_tb(flotte_db)
	mycursor.close()

#	DELETE DATABASE
def delete_flotte_db(flotte_db):
	sql="DROP DATABASE IF EXISTS flotte_db"
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print("BDD:     ", mycursor.rowcount,"DATABASE DESTROYED **explosion**")
	mycursor.close()

def use_db(flotte_db):
	mycursor=flotte_db.cursor()
	mycursor.execute("USE flotte_db")
	mycursor.close()
