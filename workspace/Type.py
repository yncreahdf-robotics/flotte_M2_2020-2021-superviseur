import mysql.connector

hosts = open('/etc/hosts','r')
for line in hosts:
	splitted_line=line.split()
	try:
		if splitted_line[1]=="supIP":
			my_ip = splitted_line[0]
	except IndexError:
		pass
#########################################
##  Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Type_tb():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		) 
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		#	Role can be: Preparateur, Service, Accueil, Guide 
		mycursor.execute("CREATE TABLE IF NOT EXISTS Type_tb (TypeID INT AUTO_INCREMENT, TypeName VARCHAR(30) UNIQUE, Role VARCHAR(30), WeightCapacity INT, CONSTRAINT TypeID_pk PRIMARY KEY (TypeID))" ) 
		#mycursor.execute(requete)
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Type_tb():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")	
		myresult=mycursor.execute("SHOW TABLES")
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT TYPES IN THE COMMAND DATABASE
def insert_Type(TypeName, Role, WeightCapacity):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="INSERT INTO Type_tb (TypeName, Role, WeightCapacity) VALUES(%s,%s,%s)"
		val=(TypeName, Role, WeightCapacity)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql,val)
		flotte_db.commit()
		print("BDD:     ", mycursor.rowcount,"Type ajouté")
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		if (format(err).split()[0]=="1062"):
			pass
		else:
			print("Something went wrong: {}".format(err))

####################################
##  Fonctions d'accès à la table  ##
####################################

#	GET ALL POSSIBLE TYPES
def get_all_Type():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="SELECT * FROM Type_tb ORDER BY TypeName"
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#get a type by its name
def get_Type(TypeName):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="SELECT * FROM Type_tb WHERE TypeName=\""+ TypeName +"\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET A TYPE BY ITS NAME IF EXISTS
def Type_exists(TypeName):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT * FROM Type_tb WHERE TypeName=\"" + TypeName + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		if len(myresult)!=0:
			return True
		return False	
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

################################
##  Fonctions de suppression  ##
################################

#	DELETE A TYPE
def delete_Type(TypeName):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="DELETE FROM Type_tb WHERE TypeName="+TypeName
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"Type deleted")
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


