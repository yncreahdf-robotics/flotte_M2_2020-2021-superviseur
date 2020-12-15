import mysql.connector


#	CREATE A NEW DATABASE
def create_flotte_db(flotte_db):	
	try:
		mycursor=flotte_db.cursor()
		mycursor.execute("CREATE DATABASE IF NOT EXISTS flotte_db")
		mycursor.execute("USE flotte_db")
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	Check if database exists
def check_flotte_db(flotte_db):
	try:
		mycursor=flotte_db.cursor()
		myresult=mycursor.execute("SHOW DATABASES")
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


#	CREATE A NEW TABLE
def create_Ordre_tb(flotte_db):
	try:
		mycursor=flotte_db.cursor()
		mycursor.execute("CREATE TABLE IF NOT EXISTS Ordre_tb (OrdreID INT AUTO_INCREMENT, OrdreName VARCHAR(30), CONSTRAINT OrdreID_pk PRIMARY KEY (OrdreID))" ) 
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Ordre_tb(flotte_db):	
	try:
		mycursor=flotte_db.cursor()
		myresult=mycursor.execute("SHOW TABLES")
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


#	INSERT ARTICLES IN THE Ordre DATABASE
def insert_Ordre(flotte_db, CommandNbr, PositionID, Prix):
	try:
		#need to verify that the articleID is an existing article in the article database
		sql="INSERT INTO Ordre_tb (OrdreID, OrdreName) VALUES(%s,%s)"
		val=(OrdreID, OrdreName)
		mycursor=flotte_db.cursor()
		mycursor.execute(sql,val)
		flotte_db.commit()
		print(mycursor.rowcount,"Ordre ajouté à la Table")
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET ALL POSSIBLE ARTICLES

#	GET ALL TABLES
def get_Ordres(flotte_db):
	try:
		sql = "SELECT * FROM Ordre_tb"
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

def get_Ordre(flotte_db, OrdreID):
	try:
		sql = "SELECT * FROM Ordre_tb WHERE OrdreID="+str(OrdreID)
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	DELETE A Ordre
def delete_Ordre(flotte_db, OrdreID):
	try:
		sql="DELETE FROM Ordre_tb WHERE OrdreID="+str(OrdreID)
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"Ordre deleted")
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

def delete_flotte_db(flotte_db):
	try:
		sql="DROP DATABASE IF EXISTS flotte_db"
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"DATABASE DESTROYED")
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

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


	

