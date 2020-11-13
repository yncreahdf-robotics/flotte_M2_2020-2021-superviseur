import mysql.connector


#	CREATE A NEW TABLE
def create_Table_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS Table_tb (TableID INT AUTO_INCREMENT, CommandNbr INT, PositionID INT, Prix FLOAT, CONSTRAINT TableID_pk PRIMARY KEY (TableID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Table_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT ARTICLES IN THE Table DATABASE
def insert_Table(mycursor, CommandNbr, PositionID, Prix):
	#need to verify that the articleID is an existing article in the article database
	sql="INSERT INTO Table_tb (CommandNbr, PositionID, Prix) VALUES(%s,%s,%s)"
	val=(CommandNbr, PositionID, Prix)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Table ajouté à la Table")

#	GET ALL POSSIBLE ARTICLES

#	GET ALL TABLES
def get_Tables(mycursor):
	sql = "SELECT * FROM Table_tb"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

def get_Table(mycursor, PositionID):
	sql = "SELECT * FROM Table_tb WHERE PositionID="+str(PositionID)
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A Table
def delete_Table(mycursor, PositionID):
	sql="DELETE FROM Table_tb WHERE PositionID="+str(PositionID)
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Table deleted")

def delete_flotte_db(mycursor):
	sql="DROP DATABASE IF EXISTS flotte_db"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED")



