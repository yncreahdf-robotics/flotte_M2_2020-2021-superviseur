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
def create_Table_tb():
	mycursor.execute("CREATE TABLE IF NOT EXISTS Table_tb (TableID INT AUTO_INCREMENT, CommandNbr INT, PositionID INT, Prix FLOAT, CONSTRAINT TableID_pk PRIMARY KEY (TableID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Table_tb():	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT ARTICLES IN THE Table DATABASE
def insert_Table(CommandNbr, PositionID, Prix):
	#need to verify that the articleID is an existing article in the article database
	sql="INSERT INTO Table_tb (CommandNbr, PositionID, Prix) VALUES(%s,%s,%s)"
	val=(CommandNbr, PositionID, Prix)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Table ajouté à la Table")

#	GET ALL POSSIBLE ARTICLES

#	GET ALL TABLES
def get_Tables():
	sql = "SELECT * FROM Table_tb"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

def get_Table(PositionID):
	sql = "SELECT * FROM Table_tb WHERE PositionID="+str(PositionID)
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A Table
def delete_Table(PositionID):
	sql="DELETE FROM Table_tb WHERE PositionID="+str(PositionID)
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Table deleted")

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
	create_Table_tb()
	check_Table_tb()
	
	insert_Table(1,1,18.50)	
	insert_Table(2,2,304.90)
	insert_Table(3,4,5)

	get_Table(2)

	delete_flotte_db()


	

