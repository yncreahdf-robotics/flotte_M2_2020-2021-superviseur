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
def create_Article_tb():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute("CREATE TABLE IF NOT EXISTS Article_tb (ArticleID INT AUTO_INCREMENT, ArticleName VARCHAR(30) UNIQUE, ArticlePrice INT, ArticleWeight INT, IDRecette INT,CONSTRAINT ArticleID_pk PRIMARY KEY (ArticleID))" ) 
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Article_tb():	
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
def insert_Article(ArticleName, ArticlePrice, ArticleWeight, IDRecette):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="INSERT INTO Article_tb (ArticleName, ArticlePrice, ArticleWeight, IDRecette) VALUES(%s,%s,%s,%s)"
		val=(ArticleName,ArticlePrice,ArticleWeight,IDRecette)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql,val)
		flotte_db.commit()
		print("BDD:	",mycursor.rowcount,"Article ajouté au menu")
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

#	GET ALL POSSIBLE ARTICLES
def get_all_Articles():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="SELECT ArticleID FROM Article_tb ORDER BY ArticleName"
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

#	GET AN ARTICLE BY ITS NAME
def get_Article_by_ID(ArticleID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)	
		sql = "SELECT * FROM Article_tb WHERE ArticleID= \"" + ArticleID + "\""
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

		#	GET AN ARTICLE BY ITS WEIGHT
def get_Article_by_Weight(ArticleID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)	
		sql = "SELECT ArticleWeight FROM Article_tb WHERE ArticleID= \"" + ArticleID + "\""
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

		# GET THE TOTAL WEIGHT OF AN ORDER
def total_weight_of_an_order(CommandNbr):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="SELECT SUM(ArticleWeight) AS total_weight FROM Article_tb INNER JOIN Commande_tb ON Article_tb.ArticleID=Commande_tb.ArticleID WHERE Commande_tb.CommandNbr = \"" + str(CommandNbr) + "\""

		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult=mycursor.fetchall()
		for x in myresult:
			x=int(x)
			print(x)
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))		


########################################################
##  Fonctions de suppression d'un article de la base  ##
########################################################

#	DELETE AN ARTICLE
def delete_Article(ArticleID): 
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)	
		sql="DELETE FROM Article_tb WHERE ArticleID=" + ArticleID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"Article deleted")
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))




