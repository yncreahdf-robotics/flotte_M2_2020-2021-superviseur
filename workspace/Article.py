import mysql.connector


#	CREATE A NEW TABLE
def create_Article_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS Article_tb (ArticleID INT AUTO_INCREMENT, ArticleName VARCHAR(30), ArticlePrice INT, ArticleWeight INT, CONSTRAINT ArticleID_pk PRIMARY KEY (ArticleID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_Article_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_Article(flotte_db,ArticleName, ArticlePrice, ArticleWeight):
	sql="INSERT INTO Article_tb (ArticleName, ArticlePrice, ArticleWeight) VALUES(%s,%s,%s)"
	val=(ArticleName,ArticlePrice,ArticleWeight)
	mycursor=flotte_db.cursor()
	mycursor.execute(sql,val)
	flotte_db.commit()
	print(mycursor.rowcount,"Article ajouté au menu")

#	GET ALL POSSIBLE ARTICLES
def get_all_Articles(mycursor):
	sql="SELECT * FROM Article_tb ORDER BY ArticleName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET AN ARTICLE BY ITS NAME
def get_Article_by_name(mycursor, ArticleName):
	sql = "SELECT * FROM Article_tb WHERE ArticleName=" + ArticleName
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE AN ARTICLE
def delete_Article(flotte_db, ArticleName):
	sql="DELETE FROM Article_tb WHERE ArticleName="+ArticleName
	mycursor=flotte_db.cursor()
	mycursor.execute(sql)
	flotte_db.commit()
	print(mycursor.rowcount,"Article deleted")





