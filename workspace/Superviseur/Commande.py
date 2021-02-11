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
##	Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Commande_tb():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		#	Etat can be Pending, Ordered, Prepared, Charged, Delivered 
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute("CREATE TABLE IF NOT EXISTS Commande_tb (CommandID INT AUTO_INCREMENT, CommandNbr INT, ArticleID INT, Etat VARCHAR(30), CONSTRAINT CommandID_pk PRIMARY KEY (CommandID))" ) 
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Commande_tb():
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

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_Commande(CommandNbr, ArticleID, Etat):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="INSERT INTO Commande_tb (CommandNbr, ArticleID,Etat) VALUES(%s,%s,%s)"
		val=(CommandNbr, ArticleID, Etat)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql,val)
		flotte_db.commit()
		mycursor.close()
		flotte_db.close()
		print("BDD:     ", mycursor.rowcount,"Article Ajouté à la commande")
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

####################################
##  Fonctions d'accès à la table  ##
####################################

#	GET ALL ARTICLES LINKED TO A COMMAND
def get_Commande(CommandNbr):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT CommandID FROM Commande_tb WHERE CommandNbr=\""+str(CommandNbr)+"\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err)) 

#	GET ARTICLES IN A COMMAND WITH A PARTICULAR STATUS
def get_Commande_with_status_and_commandNbr(CommandNbr, Status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT CommandID FROM Commande_tb WHERE CommandNbr=\""+ str(CommandNbr)+"\" AND Etat=\"" + Status +"\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")	
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET ARTICLES OF A COMMAND WITH A GIVEN STATUS
def get_CommandNbr_with_status(Status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT CommandNbr FROM Commande_tb WHERE Etat= \"" + Status +"\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		flotte_db.commit()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET QUANITIES FOR A GIVEN ARTICLE
def get_Bouteille(CommandID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT Bouteille1, Bouteille2, Bouteille3, Bouteille4, Bouteille5, Bouteille6 FROM Article_tb INNER JOIN Command_tb ON Article_tb.ArticleID=Commande_tb.ArticleID WHERE CommandID=\"" + CommandID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))	

#GET A COMMAND DATA BY ITS ID
def get_commande_data(CommandID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="SELECT * FROM Commande_tb WHERE CommandID=\""+ CommandID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")	
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

def get_commande_Nbr_status(status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="SELECT * FROM Commande_tb WHERE Etat=\""+ status + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")	
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

############################################
##	Fonctions de mise à jour de la table  ##
############################################

#	UPDATE ALL ARTICLES IN A COMMAND TO A GIVEN STATUS
def update_status(CommandNbr, Status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "UPDATE Commande_tb SET Etat = \"" + Status + "\" WHERE CommandNbr = \"" + str(CommandNbr) + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")	
		mycursor.execute(sql)
		mycursor.close()
		flotte_db.commit()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

def update_status_when_status(CommandNbr,ActualStatus, Status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "UPDATE Commande_tb SET Etat = \"" + Status + "\" WHERE CommandNbr = \"" + str(CommandNbr) + "\" AND Etat =  \"" + ActualStatus + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")	
		mycursor.execute(sql)
		mycursor.close()
		flotte_db.commit()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	UPDATE A GIVEN ORDERED ARTICLE TO A GIVEN STATUS
def update_Commande_status_by_article(CommandID ,Status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "UPDATE Commande_tb SET Etat = \"" + Status + "\" WHERE CommandID = \"" + str(CommandID) + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")	
		mycursor.execute(sql)
		mycursor.close()
		flotte_db.commit()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


########################################################
##  Fonction de suppression d'un élément de la table  ##
########################################################

#	DELETE A COMMAND
def delete_Commande(CommandNbr):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="DELETE FROM Commande_tb WHERE CommandNbr=\""+ str(CommandNbr) + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"Command deleted")
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))




