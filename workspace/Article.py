import mysql.connector

#	CREATE A NEW DATABASE
def create_command_db():	
	mycursor=command_db.cursor()
	mycursor.execute("CREATE DATABASE IF NOT EXISTS command_db")
	mycursor.execute("USE command_db")

#	Check if database exists
def check_command_db():
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)

#	CREATE A NEW TABLE
def create_article_tb():
	mycursor.execute("CREATE TABLE IF NOT EXISTS article_tb (ArticleID INT AUTO_INCREMENT, ArticleName VARCHAR(30), ArticlePrice INT, ArticleWeight INT, CONSTRAINT ArticleID_pk PRIMARY KEY (ArticleID))" ) 

#	CHECK IF THE TABLE EXISTS
def check_article_tb():	
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

#	INSERT ARTICLES IN THE COMMAND DATABASE
def insert_article(ArticleName, ArticlePrice, ArticleWeight):
	#need to verify that the articleID is an existing article in the article database
	sql="INSERT INTO article_tb (ArticleName, ArticlePrice, ArticleWeight) VALUES(%s,%s,%s)"
	val=(ArticleName,ArticlePrice,ArticleWeight)
	mycursor.execute(sql,val)
	command_db.commit()
	print(mycursor.rowcount,"article ajouté au menu")

#	GET ALL POSSIBLE ARTICLES
def get_all_Articles():
	sql="SELECT * FROM article_tb ORDER BY ArticleName"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	for x in myresult:
		print(x)


#	GET AN ARTICLE BY ITS NAME
def get_Article_by_name(ArticleName):
	sql = "SELECT * FROM article_tb WHERE ArticleName=ArticleName IF EXISTS"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

#	DELETE AN ARTICLE
def delete_Article(ArticleName):
	sql="DELETE FROM article_tb WHERE ArticleName=ArticleName"
	mycursor.execute(sql)
	command_db.commit()
	print(mycursor.rowcount,"Article deleted")

def delete_command_db():
	sql="DROP DATABASE command_db"
	mycursor.execute(sql)
	command_db.commit()
	print(mycursor.rowcount,"DATABASE DESTROYED **explosion**")

if __name__ == '__main__':

	#initialisation 
	command_db=mysql.connector.connect(
		host='localhost',
		user='root',
		password='password'
		)
	mycursor=command_db.cursor()

	create_command_db()
	check_command_db()

	create_article_tb()
	check_article_tb()


	insert_article('Coca Cola', 2, 50)
	insert_article('Whisky',3, 10)
	insert_article('Jagger', 1, 100)
	get_all_Articles();
	delete_Article('Whisky')
	delete_command_db()
