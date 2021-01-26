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
def create_Recette_tb():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute("CREATE TABLE IF NOT EXISTS Recette_tb (RecetteID INT AUTO_INCREMENT, RecetteName VARCHAR(30) UNIQUE, BouteilleID1 INT, Quantity1 INT, BouteilleID2 INT, Quantity2 INT, BouteilleID3 INT, Quantity3 INT, BouteilleID4 INT, Quantity4 INT, BouteilleID5 INT, Quantity5 INT, BouteilleID6 INT, Quantity6 INT,CONSTRAINT RecetteID_pk PRIMARY KEY (RecetteID))" ) 
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Recette_tb():	
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
def insert_Recette(RecetteName, BouteilleID1, Quantity1, BouteilleID2, Quantity2, BouteilleID3, Quantity3, BouteilleID4, Quantity4, BouteilleID5, Quantity5, BouteilleID6, Quantity6):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="INSERT INTO Recette_tb (RecetteName, BouteilleID1, Quantity1, BouteilleID2, Quantity2, BouteilleID3, Quantity3, BouteilleID4, Quantity4, BouteilleID5, Quantity5, BouteilleID6, Quantity6) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val=(RecetteName, BouteilleID1, Quantity1, BouteilleID2, Quantity2, BouteilleID3, Quantity3, BouteilleID4, Quantity4, BouteilleID5, Quantity5, BouteilleID6, Quantity6)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql,val)
		flotte_db.commit()
		print("BDD:	",mycursor.rowcount,"Recette ajoutée")
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

#	GET ALL POSSIBLE RECETTES
def get_all_Recettes():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="SELECT RecetteID FROM Recette_tb"
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

#	GET A Bouteille BY ITS ID
def get_Recette_by_ID(BouteilleID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)	
		sql = "SELECT * FROM Bouteille_tb WHERE RecetteID= \"" + RecetteID + "\""
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