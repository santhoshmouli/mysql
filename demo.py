import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="santhosh mouli",passwd="santhoshmouli123",database="santhoshmouli")
mycursor = mydb.cursor()
mycursor.execute("select * from student")
result=mycursor.fetchall()
for i in result:
    print(i)