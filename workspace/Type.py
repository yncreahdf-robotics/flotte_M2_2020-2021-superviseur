import mysql.connector


#########################################
##  Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Type_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS Type_tb (TypeID INT AUTO_INCREMENT, TypeName VARCHAR(30), Role VARCHAR(30), WeightCapacity INT, CONSTRAINT TypeID_pk PRIMARY KEY (TypeID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Type_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT TYPES IN THE COMMAND DATABASE
def insert_Type(flotte_db, TypeName, Role, WeightCapacity):
	sql="INSERT INTO Type_tb (TypeName, Role, WeightCapacity) VALUES(%s,%s,%s)"
	val=(TypeName, Role, WeightCapacity)
	mycursor=flotte_db.cursor()
	mycursor.execute(sql,val)
	flotte_db.commit()
	print("BDD:     ", mycursor.rowcount,"Type ajouté")

####################################
##  Fonctions d'accès à la table  ##
####################################

#	GET ALL POSSIBLE TYPES
def get_all_Type(mycursor):
	sql="SELECT * FROM Type_tb ORDER BY TypeName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	return myresult

#	GET A TYPE BY ITS NAME IF EXISTS
def Type_exists(mycursor, TypeName):
	sql = "SELECT * FROM Type_tb WHERE TypeName=\"" + TypeName + "\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	if len(myresult)!=0:
		return True
	return False

################################
##  Fonctions de suppression  ##
################################

#	DELETE A TYPE
def delete_Type(flotte_db, TypeName):
	sql="DELETE FROM Type_tb WHERE TypeName="+TypeName
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Type deleted")



