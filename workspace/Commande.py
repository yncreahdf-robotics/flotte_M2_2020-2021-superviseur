import mysql.connector

#########################################
##	Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Commande_tb(mycursor):
	#	Etat can be Pending, Ordered, Prepared, Charged, Delivered 
	mycursor.execute("CREATE TABLE IF NOT EXISTS Commande_tb (CommandID INT AUTO_INCREMENT, CommandNbr INT, ArticleID INT, Etat VARCHAR(30), CONSTRAINT CommandID_pk PRIMARY KEY (CommandID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Commande_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_Commande(flotte_db, CommandNbr,ArticleID,Etat):
	#need to verify that the articleID is an existing article in the article database
	sql="INSERT INTO Commande_tb (CommandNbr, ArticleID, Etat) VALUES(%s,%s,%s)"
	val=(CommandNbr,ArticleID,Etat)
	mycursor=flotte_db.cursor()
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"article ajouté à la commande")

####################################
##  Fonctions d'accès à la table  ##
####################################

#	GET ALL ARTICLES LINKED TO A COMMAND
def get_Commande(mycursor, CommandNbr):
	sql = "SELECT * FROM Commande_tb WHERE CommandNbr=\""+CommandNbr+"\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult 

#	GET ARTICLES IN A COMMAND WITH A PARTICULAR STATUS
def get_Commande_with_status_and_commandNbr(mycursor, CommandNbr, Status):
	sql = sql = "SELECT * FROM Commande_tb WHERE CommandNbr=\""+CommandNbr+"\" AND Etat=\"" + Status +"\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult

#	GET ARTICLES OF A GIVEN COMMAND WITH A GIVEN STATUS
def get_CommandNbr_with_status(mycursor, Status):
	sql = sql = "SELECT CommandNbr FROM Commande_tb WHERE Etat=\"" + Status +"\""
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	return myresult

############################################
##	Fonctions de mise à jour de la table  ##
############################################

#	UPDATE ALL ARTICLES IN A COMMAND TO A GIVEN STATUS
def update_Commande_status(mycursor, CommandNbr, Status):
	sql = "UPDATE Commande_tb SET Etat = \"" + Status + "\" WHERE CommandNbr = \'" + CommandNbr + "\""
	mycursor.execute(sql)

#	UPDATE A GIVEN ORDERED ARTICLE TO A GIVEN STATUS
def update_Commande_status_by_article(mycursor, CommandID ,Status):
	sql = "UPDATE Commande_tb SET Etat = \"" + Status + "\" WHERE CommandID = \"" + CommandID + "\""
	mycursor.execute(sql)

########################################################
##  Fonction de suppression d'un élément de la table  ##
########################################################

#	DELETE A COMMAND
def delete_Commande(flotte_db, CommandNbr):
	sql="DELETE FROM Commande_tb WHERE CommandNbr="+CommandNbr
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Command deleted")




