import mysql.connector

#########################################
##	Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Commande_tb(flotte_db):
	#	Etat can be Pending, Ordered, Prepared, Charged, Delivered 
	mycursor=flotte_db.cursor()
	mycursor.execute("CREATE TABLE IF NOT EXISTS Commande_tb (CommandID INT AUTO_INCREMENT, CommandNbr INT, ArticleID INT, Etat VARCHAR(30), CONSTRAINT CommandID_pk PRIMARY KEY (CommandID))" ) 
	mycursor.close()

#	CHECK IF THE TABLE EXISTS
def check_Commande_tb(flotte_db):	
	mycursor=flotte_db.cursor()
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)
	mycursor.close()


############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_Commande(flotte_db, CommandNbr, ArticleID, Etat):
	sql="INSERT INTO Commande_tb (CommandNbr, ArticleID,Etat) VALUES(%s,%s,%s)"
	val=(CommandNbr, ArticleID, Etat)
	mycursor=flotte_db.cursor()
	mycursor.execute(sql,val)
	flotte_db.commit()
	mycursor.close()
	print("BDD:     ", mycursor.rowcount,"Article Ajouté à la commande")

####################################
##  Fonctions d'accès à la table  ##
####################################

#	GET ALL ARTICLES LINKED TO A COMMAND
def get_Commande(flotte_db, CommandNbr):
	sql = "SELECT CommandID FROM Commande_tb WHERE CommandNbr=\""+CommandNbr+"\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	mycursor.close()
	return myresult 

#	GET ARTICLES IN A COMMAND WITH A PARTICULAR STATUS
def get_Commande_with_status_and_commandNbr(flotte_db, CommandNbr, Status):
	sql = "SELECT CommandID FROM Commande_tb WHERE CommandNbr=\""+ str(CommandNbr)+"\" AND Etat=\"" + Status +"\""
	mycursor=flotte_db.cursor()	
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	mycursor.close()
	return myresult

#	GET ARTICLES OF A COMMAND WITH A GIVEN STATUS
def get_CommandNbr_with_status(flotte_db, Status):
	sql = "SELECT CommandNbr FROM Commande_tb WHERE Etat= \"" + Status +"\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	flotte_db.commit()
	mycursor.close()
	return myresult

#	GET QUANITIES FOR A GIVEN ARTICLE
def get_Bouteille(flotte_db, CommandID):
	sql = "SELECT Bouteille1, Bouteille2, Bouteille3, Bouteille4, Bouteille5, Bouteille6 FROM Article_tb INNER JOIN Command_tb ON Article_tb.ArticleID=Commande_tb.ArticleID WHERE CommandID=\"" + CommandID + "\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	mycursor.close()
	return myresult


############################################
##	Fonctions de mise à jour de la table  ##
############################################

#	UPDATE ALL ARTICLES IN A COMMAND TO A GIVEN STATUS
def update_status(flotte_db, CommandNbr, Status):
	sql = "UPDATE Commande_tb SET Etat = \"" + Status + "\" WHERE CommandNbr = \"" + str(CommandNbr) + "\""
	mycursor=flotte_db.cursor()	
	mycursor.execute(sql)
	mycursor.close()

#	UPDATE A GIVEN ORDERED ARTICLE TO A GIVEN STATUS
def update_Commande_status_by_article(flotte_db, CommandID ,Status):
	sql = "UPDATE Commande_tb SET Etat = \"" + Status + "\" WHERE CommandID = \"" + CommandID + "\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	mycursor.close()

########################################################
##  Fonction de suppression d'un élément de la table  ##
########################################################

#	DELETE A COMMAND
def delete_Commande(flotte_db, CommandNbr):
	sql="DELETE FROM Commande_tb WHERE CommandNbr=\""+ CommandNbr + "\""
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Command deleted")
	mycursor.close()




