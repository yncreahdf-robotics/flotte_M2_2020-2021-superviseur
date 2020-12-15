import mysql.connector

#########################################
##  Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Table_tb(flotte_db):
	try:
		#Etat can be Free/Occupied
		mycursor=flotte_db.cursor()
		mycursor.execute("CREATE TABLE IF NOT EXISTS Table_tb (TableID INT AUTO_INCREMENT, CommandNbr INT, PositionID INT, Place INT, Etat VARCHAR(30),Prix FLOAT, CONSTRAINT TableID_pk PRIMARY KEY (TableID))" ) 
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Table_tb(flotte_db):	
	try:
		mycursor.execute("SHOW TABLES")
		for x in mycursor:
			print(x)
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT ARTICLES IN THE TABLE DATABASE
def insert_Table(flotte_db, CommandNbr, PositionID, Place, Etat, Prix):
	try:
		sql="INSERT INTO Table_tb (CommandNbr, PositionID, Place, Etat, Prix) VALUES(%s,%s,%s,%s,%s)"
		val=(CommandNbr, PositionID, Place, Etat, Prix)
		mycursor=flotte_db.cursor()
		mycursor.execute(sql,val)
		flotte_db.commit()
		mycursor.close()
		print("BDD: 	Table ajoutée")
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

####################################
##  Fonctions d'accès à la table  ##
####################################

#	GET ALL TABLES
def get__all_Table(flotte_db):
	try:
		sql = "SELECT * FROM Table_tb"
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

# 	GET A TABLE BY ID
def get_Table_data(flotte_db, TableID):
	try:
		sql = "SELECT * FROM Table_tb WHERE TableID=\"" + TableID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET A TABLE BY NUMBER OF PLACES AND STATUS
def get_Table_Nbr_and_Status(flotte_db, Place, Status):
	try:
		sql = "SELECT TableID FROM Table_tb WHERE Place <= \"" + Place + "\" AND Etat = \"" + Status + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET THE NUMBER OF ARTICLE TO BE CHARGED
def get_remaining_charge_Table(flotte_db, TableID):
	try:
		#	On cherche le nombre d'articles à charger 
		sql = "SELECT CommandNbr FROM Commande_tb INNER JOIN Table_tb ON Commande_tb.CommandNbr=Table_tb.CommandNbr WHERE Command_tb.Etat= \"Prepared\" AND Table_tb.TableID=\""+TableID+"\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		return len(myresult)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


############################################
##	Fonctions de mise à jour de la table  ##
############################################

def update_Table_commandNbr(flotte_db, TableID, CommandNbr):
	try:
		sql = "UPDATE Table_tb SET CommandNbr = \"" + CommandNbr + "\" WHERE TableID = \'" + TableID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

def update_Table_price(flotte_db, TableID, Prix):
	try:
		sql = "UPDATE Table_tb SET Prix = \"" + Prix + "\" WHERE TableID = \'" + TableID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

def update_Table_status(flotte_db, TableID, Status):
	try:
		sql = "UPDATE Table_tb SET Etat = \"" + Status + "\" WHERE TableID = \'" + TableID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

############################################
##  Fonctions de suppression de la table  ##
############################################

#	DELETE A TABLE
def delete_Table(flotte_db, TableID):
	try:
		sql="DELETE FROM Table_tb WHERE TableID=\"" + TableID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"Table deleted")
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))



