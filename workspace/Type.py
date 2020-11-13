import mysql.connector

#	CREATE A NEW TABLE
def create_Type_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS Type_tb (TypeID INT AUTO_INCREMENT, TypeName VARCHAR(30), Role VARCHAR(30), WeightCapacity INT, CONSTRAINT TypeID_pk PRIMARY KEY (TypeID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Type_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT TYPES IN THE COMMAND DATABASE
def insert_Type(mycursor, TypeName, Role, WeightCapacity):
	sql="INSERT INTO Type_tb (TypeName, Role, WeightCapacity) VALUES(%s,%s,%s)"
	val=(TypeName, Role, WeightCapacity)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Type ajouté")

#	GET ALL POSSIBLE TYPES
def get_all_Type(mycursor):
	sql="SELECT * FROM Type_tb ORDER BY TypeName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET A TYPE BY ITS NAME
def get_Type_by_name(mycursor, TypeName):
	sql = "SELECT * FROM Type_tb WHERE TypeName="+TypeName+" IF EXISTS"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A TYPE
def delete_Type(mycursor, TypeName):
	sql="DELETE FROM Type_tb WHERE TypeName="+TypeName
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Type deleted")



