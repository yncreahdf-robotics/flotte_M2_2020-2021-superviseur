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
def create_Ordre_tb():
	mycursor.execute("CREATE TABLE IF NOT EXISTS Ordre_tb (OrdreID INT AUTO_INCREMENT, OrdreName VARCHAR(30), CONSTRAINT OrdreID_pk PRIMARY KEY (OrdreID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Ordre_tb():	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT ARTICLES IN THE Ordre DATABASE
def insert_Ordre(CommandNbr, PositionID, Prix):
	#need to verify that the articleID is an existing article in the article database
	sql="INSERT INTO Ordre_tb (OrdreID, OrdreName) VALUES(%s,%s)"
	val=(OrdreID, OrdreName)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Ordre ajouté à la Table")

#	GET ALL POSSIBLE ARTICLES

#	GET ALL TABLES
def get_Ordres():
	sql = "SELECT * FROM Ordre_tb"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

def get_Ordre(OrdreID):
	sql = "SELECT * FROM Ordre_tb WHERE OrdreID="+str(OrdreID)
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A Ordre
def delete_Ordre(OrdreID):
	sql="DELETE FROM Ordre_tb WHERE OrdreID="+str(OrdreID)
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Ordre deleted")

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
	create_Ordre_tb()
	check_Ordre_tb()
	

	delete_flotte_db()


	

