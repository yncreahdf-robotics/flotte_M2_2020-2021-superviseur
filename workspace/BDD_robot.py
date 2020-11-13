import mysql.connector
import Article
import Commande
import Table
import Type
import Robot
import Positions


#	Check if database exists
def check_flotte_db(mycursor):
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)


#	Initialisation

###	CONNECTS TO DATABASE	### 
flotte_db=mysql.connector.connect(
	host='192.168.1.5',
	database='flotte_db',
	user='robot',
	password='robot'
)
global mycursor
mycursor=flotte_db.cursor()


#############################
#####	CODE ROBOT	#####
#####	READ ONLY	#####
#############################
# exemple Article.get_all_articles(mycursor)

