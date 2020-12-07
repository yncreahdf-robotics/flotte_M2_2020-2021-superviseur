import mysql.connector

#########################################
##  Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Table_tb(mycursor):
	#Etat can be Free/Occupied
	mycursor.execute("CREATE TABLE IF NOT EXISTS Table_tb (TableID INT AUTO_INCREMENT, CommandNbr INT, PositionID INT, Place INT, Etat VARCHAR(30),Prix FLOAT, CONSTRAINT TableID_pk PRIMARY KEY (TableID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Table_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT ARTICLES IN THE TABLE DATABASE
def insert_Table(mycursor, CommandNbr, PositionID, Place, Etat, Prix):
	sql="INSERT INTO Table_tb (CommandNbr, PositionID, Place, Etat, Prix) VALUES(%s,%s,%s,%s,%s)"
	val=(CommandNbr, PositionID, Place, Etat, Prix)
	mycursor.execute(sql,val)
	print("BDD: 	Table ajoutée")

####################################
##  Fonctions d'accès à la table  ##
####################################

#	GET ALL TABLES
def get__all_Table(mycursor):
	sql = "SELECT * FROM Table_tb"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult

# 	GET A TABLE BY ID
def get_Table_data(mycursor, TableID):
	sql = "SELECT * FROM Table_tb WHERE TableID=\"" + TableID + "\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult

#	GET A TABLE BY NUMBER OF PLACES AND STATUS
def get_Table_Nbr_and_Status(mycursor, Place, Status):
	sql = "SELECT TableID FROM Table_tb WHERE Place <= \"" + Place + "\" AND Etat = \"" + Status + "\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult

#	GET THE NUMBER OF ARTICLE TO BE CHARGED
def get_remaining_charge_Table(mycursor, TableID):
	#	On cherche le nombre d'articles à charger 
	sql = "SELECT CommandNbr FROM Commande_tb INNER JOIN Table_tb ON Commande_tb.CommandNbr=Table_tb.CommandNbr WHERE Command_tb.Etat= \"Prepared\" AND Table_tb.TableID=\""+TableID+"\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return len(myresult)


############################################
##	Fonctions de mise à jour de la table  ##
############################################

def update_Table_commandNbr(mycursor, TableID, CommandNbr):
	sql = "UPDATE Table_tb SET CommandNbr = \"" + CommandNbr + "\" WHERE TableID = \'" + TableID + "\""
	mycursor.execute(sql)

def update_Table_price(mycursor, TableID, Prix):
	sql = "UPDATE Table_tb SET Prix = \"" + Prix + "\" WHERE TableID = \'" + TableID + "\""
	mycursor.execute(sql)

def update_Table_status(mycursor, TableID, Status):
	sql = "UPDATE Table_tb SET Etat = \"" + Status + "\" WHERE TableID = \'" + TableID + "\""
	mycursor.execute(sql)


############################################
##  Fonctions de suppression de la table  ##
############################################

#	DELETE A TABLE
def delete_Table(flotte_db, TableID):
	sql="DELETE FROM Table_tb WHERE TableID=\"" + TableID + "\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Table deleted")




