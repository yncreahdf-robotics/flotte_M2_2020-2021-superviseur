import mysql.connector


#	CREATE A NEW TABLE
def create_command_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS command_tb (CommandID INT AUTO_INCREMENT, CommandNbr INT, ArticleID INT, ArticleQtt INT, CONSTRAINT CommandID_pk PRIMARY KEY (CommandID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_command_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_command(mycursor, CommandNbr,ArticleID,ArticleQtt):
	#need to verify that the articleID is an existing article in the article database
	sql="INSERT INTO command_tb (CommandNbr, ArticleID, ArticleQtt) VALUES(%s,%s,%s)"
	val=(CommandNbr,ArticleID,ArticleQtt)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"article ajouté à la commande")

#	GET ALL POSSIBLE ARTICLES

#	GET ALL ARTICLES LINKED TO A COMMAND
def get_command(mycursor, CommandNbr):
	sql = "SELECT * FROM command_tb WHERE CommandNbr=CommandNbr"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A COMMAND
def delete_command(mycursor, CommandNbr):
	sql="DELETE FROM command_tb WHERE CommandNbr=CommandNbr"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Command deleted")

def delete_flotte_db(mycursor):
	sql="DROP DATABASE IF EXISTS flotte_db"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED")


