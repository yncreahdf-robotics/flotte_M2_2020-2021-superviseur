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
def create_type_tb():
	mycursor.execute("CREATE TABLE IF NOT EXISTS type_tb (TypeID INT AUTO_INCREMENT, TypeName VARCHAR(30), Role VARCHAR(30), WeightCapacity INT, CONSTRAINT TypeID_pk PRIMARY KEY (TypeID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_type_tb():	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT TYPES IN THE COMMAND DATABASE
def insert_Type(TypeName, Role, WeightCapacity):
	#need to verify that the TypeName is an existing Type in the Type database
	sql="INSERT INTO type_tb (TypeName, Role, WeightCapacity) VALUES(%s,%s,%s)"
	val=(TypeName, Role, WeightCapacity)
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"type ajouté")

#	GET ALL POSSIBLE TYPES
def get_all_Type():
	sql="SELECT * FROM type_tb ORDER BY TypeName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET A TYPE BY ITS NAME
def get_Type_by_name(TypeName):
	sql = "SELECT * FROM type_tb WHERE TypeName=TypeName IF EXISTS"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE A TYPE
def delete_Type(TypeName):
	sql="DELETE FROM type_tb WHERE TypeName=TypeName"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Type deleted")

def delete_flotte_db():
	sql="DROP DATABASE flotte_db"
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED **explosion**")

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

	create_type_tb()
	check_type_tb()


	insert_Type('Robotino', 'Service', 5000)
	insert_Type('Heron','Service', 3000)
	insert_Type('Turtlebot','Service', 2000)
	insert_Type('Niryo', 'Preparateur', 1000)
	insert_Type('Colabot', 'Accueil', 0)
	get_all_Type();
	delete_Type('Whisky')
	delete_flotte_db()
