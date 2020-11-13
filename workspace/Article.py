import mysql.connector


#	CREATE A NEW TABLE
def create_article_tb(mycursor):
	mycursor.execute("CREATE TABLE IF NOT EXISTS article_tb (ArticleID INT AUTO_INCREMENT, ArticleName VARCHAR(30), ArticlePrice INT, ArticleWeight INT, CONSTRAINT ArticleID_pk PRIMARY KEY (ArticleID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_article_tb(mycursor):	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_article(mycursor,ArticleName, ArticlePrice, ArticleWeight):
	#need to verify that the articleID is an existing article in the article database
	sql="INSERT INTO article_tb (ArticleName, ArticlePrice, ArticleWeight) VALUES(%s,%s,%s)"
	val=(ArticleName,ArticlePrice,ArticleWeight)
	mycursor.execute(sql,val)
	command_db.commit()
	print(mycursor.rowcount,"article ajouté au menu")

#	GET ALL POSSIBLE ARTICLES
def get_all_Articles(mycursor):
	sql="SELECT * FROM article_tb ORDER BY ArticleName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET AN ARTICLE BY ITS NAME
def get_Article_by_name(mycursor, ArticleName):
	sql = "SELECT * FROM article_tb WHERE ArticleName=" + ArticleName
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE AN ARTICLE
def delete_Article(mycursor, ArticleName):
	sql="DELETE FROM article_tb WHERE ArticleName=ArticleName"
	mycursor.execute(sql)
	command_db.commit()
	print(mycursor.rowcount,"Article deleted")

def delete_command_db(mycursor):
	sql="DROP DATABASE command_db"
	mycursor.execute(sql)
	command_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED **explosion**")




