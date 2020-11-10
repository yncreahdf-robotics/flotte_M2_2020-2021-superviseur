import mysql.connector


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
def create_command_tb():
	mycursor.execute("CREATE TABLE IF NOT EXISTS command_tb (CommandID INT AUTO_INCREMENT, CommandNbr INT, ArticleID INT, ArticleQtt INT, CONSTRAINT CommandID_pk PRIMARY KEY (CommandID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_command_tb():	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_command(CommandNbr,ArticleID,ArticleQtt):
	#need to verify that the articleID is an existing article in the article database
	sql="INSERT INTO command_tb (CommandNbr, ArticleID, ArticleQtt) VALUES(%s,%s,%s)"
	val=(CommandNbr,ArticleID,ArticleQtt)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"article ajouté à la commande")

#	GET ALL POSSIBLE ARTICLES

#	GET ALL ARTICLES LINKED TO A COMMAND
def get_command(CommandNbr):
	sql = "SELECT * FROM command_tb WHERE CommandNbr=CommandNbr"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A COMMAND
def delete_command(CommandNbr):
	sql="DELETE FROM command_tb WHERE CommandNbr=CommandNbr"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Command deleted")

def delete_flotte_db():
	sql="DROP DATABASE IF EXISTS flotte_db"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED")

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
	create_command_tb()
	check_command_tb()
	#delete_flotte_db()

