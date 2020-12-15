import mysql.connector

#########################################
##  Fonctions de création de la table  ##
#########################################

#	CREATE A NEW TABLE
def create_Article_tb(flotte_db):
	try:
		mycursor=flotte_db.cursor()
		mycursor.execute("CREATE TABLE IF NOT EXISTS Article_tb (ArticleID INT AUTO_INCREMENT, ArticleName VARCHAR(30), ArticlePrice INT, ArticleWeight INT, Bouteille1 INT, Bouteille2 INT, Bouteille3 INT, Bouteille4 INT, Bouteille5 INT,  Bouteille6 INT,CONSTRAINT ArticleID_pk PRIMARY KEY (ArticleID))" ) 
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Article_tb(flotte_db):	
	try:
		mycursor=flotte_db.cursor()
		mycursor.execute("SHOW TABLES")
		for x in mycursor:
			print(x)
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

############################################
##  Fonctions de remplissage de la table  ##
############################################

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_Article(flotte_db,ArticleName, ArticlePrice, ArticleWeight, Bouteille1,Bouteille2,Bouteille3,Bouteille4,Bouteille5,Bouteille6):
	try:
		sql="INSERT INTO Article_tb (ArticleName, ArticlePrice, ArticleWeight, Bouteille1,Bouteille2,Bouteille3,Bouteille4,Bouteille5,Bouteille6) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val=(ArticleName,ArticlePrice,ArticleWeight,Bouteille1,Bouteille2,Bouteille3,Bouteille4,Bouteille5,Bouteille6)
		mycursor=flotte_db.cursor()
		mycursor.execute(sql,val)
		flotte_db.commit()
		print(mycursor.rowcount,"Article ajouté au menu")
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
###################################
##	Fonctions d'accès à la table ##
###################################

#	GET ALL POSSIBLE ARTICLES
def get_all_Articles(flotte_db):
	try:
		sql="SELECT ArticleID FROM Article_tb ORDER BY ArticleName"
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		for x in myresult:
			print(x)
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET AN ARTICLE BY ITS NAME
def get_Article_by_name(flotte_db, ArticleID):
	try:	
		sql = "SELECT * FROM Article_tb WHERE ArticleID= \"" + ArticleID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)
		mycursor.close()

	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


########################################################
##  Fonctions de suppression d'un article de la base  ##
########################################################

#	DELETE AN ARTICLE
def delete_Article(flotte_db, ArticleID): 
	try:	
		sql="DELETE FROM Article_tb WHERE ArticleID=" + ArticleID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"Article deleted")
		mycursor.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))




