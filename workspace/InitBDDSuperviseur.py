import Article
import Commande
import Table
import Type
import Robot
import Positions
import mysql.connector

hosts = open('/etc/hosts','r')
for line in hosts:
	splitted_line=line.split()
	try:
		if splitted_line[1]=="supIP":
			my_ip = splitted_line[0]
	except IndexError:
		pass

#	CREATE A NEW DATABASE
def create_flotte_db():
	flotte_db=mysql.connector.connect(
		host='172.19.0.3',
		user='root',
		password='root'
	)
	mycursor=flotte_db.cursor()	
	mycursor.execute("CREATE DATABASE IF NOT EXISTS flotte_db")
	mycursor.execute("USE flotte_db")
	mycursor.close()
	flotte_db.close()
	print("BDD:	Base de données créée")

#	Check if database exists
def check_flotte_db():	
	flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
	)	
	mycursor=flotte_db.cursor()
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)
	mycursor.close()
	flotte_db.close()

#	CREATE ALL TABLES
def create_all_tables():
	Article.create_Article_tb()
	Commande.create_Commande_tb()
	Table.create_Table_tb()
	Type.create_Type_tb()
	Robot.create_Robot_tb()
	Positions.create_Pose_tb()


#	DELETE DATABASE
def delete_flotte_db():
	flotte_db=mysql.connector.connect(
		host='172.19.0.3',
		user='root',
		password='root'
	)
	sql="DROP DATABASE IF EXISTS flotte_db"
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print("BDD:     ", mycursor.rowcount,"DATABASE DESTROYED **explosion**")
	mycursor.close()
	flotte_db.close()

def use_db():
	flotte_db=mysql.connector.connect(
		host='172.19.0.3',
		user='root',
		password='root'
	)
	mycursor=flotte_db.cursor()
	mycursor.execute("USE flotte_db")
	mycursor.close()
	flotte_db.close()
