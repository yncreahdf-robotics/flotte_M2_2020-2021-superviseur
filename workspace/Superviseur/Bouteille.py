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
def create_Bouteille_tb():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute("CREATE TABLE IF NOT EXISTS Bouteille_tb (BouteilleID INT AUTO_INCREMENT, BouteilleName VARCHAR(30) UNIQUE, VolumeDoseur INT, Emplacement INT,CONSTRAINT BouteilleID_pk PRIMARY KEY (BouteilleID))" ) 
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Bouteille_tb():	
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute("SHOW TABLES")
		for x in mycursor:
			print(x)
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT BouteilleS IN THE COMMAND DATABASE
def insert_Bouteille(BouteilleName, VolumeDoseur, Emplacement):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="INSERT INTO Bouteille_tb (BouteilleName, VolumeDoseur, Emplacement) VALUES(%s,%s,%s)"
		val=(BouteilleName, VolumeDoseur, Emplacement)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql,val)
		flotte_db.commit()
		print("BDD:	",mycursor.rowcount,"Bouteille ajoutée")
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		if (format(err).split()[0]=="1062"):
			pass
		else:
			print("Something went wrong: {}".format(err))

###################################
##	Fonctions d'accès à la table ##
###################################

#	GET ALL POSSIBLE BouteilleS
def get_all_Bouteilles():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="SELECT BouteilleID FROM Bouteille_tb ORDER BY BouteilleName"
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		for x in myresult:
			print(x)
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


#	GET A Bouteille BY ITS NAME
def get_Bouteille_by_ID(BouteilleID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)	
		sql = "SELECT * FROM Bouteille_tb WHERE BouteilleID= \"" + BouteilleID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)
		mycursor.close()
		flotte_db.close()

	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


#	GET AN Bouteille BY ITS NAME
def get_Bouteille_by_Name(BouteilleName):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)	
		sql = "SELECT BouteilleID FROM Bouteille_tb WHERE BouteilleName= \"" + BouteilleName + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)
		mycursor.close()
		flotte_db.close()

	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


############################################
##	Fonctions de mise à jour de la table  ##
############################################

#UPDATE ALL BouteilleS IN A COMMAND TO A GIVEN STATUS
def update_ID(BouteilleName, newID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "UPDATE Bouteille_tb SET BouteilleID = \"" + str(newID) + "\" WHERE BouteilleName = \"" + BouteilleName + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")	
		mycursor.execute(sql)
		mycursor.close()
		flotte_db.commit()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

########################################################
##  Fonctions de suppression d'un Bouteille de la base  ##
########################################################

#	DELETE AN Bouteille
def delete_Bouteille(BouteilleID): 
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)	
		sql="DELETE FROM Bouteille_tb WHERE BouteilleID=" + BouteilleID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"Bouteille deleted")
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))