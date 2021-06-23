import pymysql
db=pymysql.connect(user="root",
                   host="localhost",
                   password="",
                   database="testpress")
cursor=db.cursor()
sql="INSERT INTO QUESTIONS(QUESTION,CORRECT,OP1,OP2,OP3,ID)VALUES('WHAT','1','2','3','4','1')"
cursor.execute(sql)
db.commit()
db.close()
