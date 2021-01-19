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
def create_Table_tb():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		#Etat can be Free/Pending/Ordered/Prepared/Charged as a group of article (commande)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute("CREATE TABLE IF NOT EXISTS Table_tb (TableID INT AUTO_INCREMENT, CommandNbr INT, PositionID INT UNIQUE, Place INT, Etat VARCHAR(30),Prix FLOAT, CONSTRAINT TableID_pk PRIMARY KEY (TableID))" ) 
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	CHECK IF THE TABLE EXISTS
def check_Table_tb():	
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
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

#	INSERT ARTICLES IN THE TABLE DATABASE
def insert_Table(CommandNbr, PositionID, Place, Etat, Prix):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="INSERT IGNORE INTO Table_tb (CommandNbr, PositionID, Place, Etat, Prix) VALUES(%s,%s,%s,%s,%s)"
		val=(CommandNbr, PositionID, Place, Etat, Prix)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql,val)
		flotte_db.commit()
		mycursor.close()
		flotte_db.close()
		print("BDD: 	Table ajoutée")
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

####################################
##  Fonctions d'accès à la table  ##
####################################

#	GET ALL TABLES
def get__all_Table():
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT * FROM Table_tb"
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

# 	GET A TABLE BY ID
def get_Table_data(TableID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT * FROM Table_tb WHERE TableID=\"" + str(TableID) + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


#	GET A TABLE BY STATUS
def get_Table_by_Status(Status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT TableID FROM Table_tb WHERE Etat = \"" + Status + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))


#	GET A TABLE BY NUMBER OF PLACES AND STATUS
def get_Table_Nbr_and_Status(Place, Status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT TableID FROM Table_tb WHERE Place <= \"" + Place + "\" AND Etat = \"" + Status + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return myresult
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET THE NUMBER OF ARTICLE TO BE CHARGED
def get_remaining_charge_Table(TableID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		#	On cherche le nombre d'articles à charger 
		sql = "SELECT CommandNbr FROM Commande_tb INNER JOIN Table_tb ON Commande_tb.CommandNbr=Table_tb.CommandNbr WHERE Command_tb.Etat= \"Prepared\" AND Table_tb.TableID=\""+TableID+"\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		mycursor.close()
		flotte_db.close()
		return len(myresult)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

#	GET A TABLE BY NUMBER OF PLACES AND STATUS
def get_Table_by_CommandNbr(CommandNbr):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "SELECT TableID FROM Table_tb WHERE CommandNbr = \"" + str(CommandNbr) + "\""
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

def update_Table_commandNbr(TableID, CommandNbr):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "UPDATE Table_tb SET CommandNbr = %s WHERE TableID = %s "
		val = (CommandNbr,TableID)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql,val)
		mycursor.close()
		flotte_db.commit()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

def update_Table_price(TableID, Prix):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "UPDATE Table_tb SET Prix = \"" + Prix + "\" WHERE TableID = \'" + TableID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		mycursor.close()
		flotte_db.commit()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

def update_Table_status(TableID, Status):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql = "UPDATE Table_tb SET Etat = %s WHERE TableID = %s "
		val = (Status,TableID)
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql,val)
		mycursor.close()
		flotte_db.commit()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

############################################
##  Fonctions de suppression de la table  ##
############################################

#	DELETE A TABLE
def delete_Table(TableID):
	try:
		flotte_db=mysql.connector.connect(
			host='172.19.0.3',
			user='root',
			password='root'
		)
		sql="DELETE FROM Table_tb WHERE TableID=\"" + TableID + "\""
		mycursor=flotte_db.cursor()
		mycursor.execute("USE flotte_db")
		mycursor.execute(sql)
		flotte_db.commit()
		print(mycursor.rowcount,"Table deleted")
		mycursor.close()
		flotte_db.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))



