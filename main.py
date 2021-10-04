import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="vageesh", passwd="1964", port="3306", database="movielist")

mycursor = mydb.cursor()

mycursor.execute("select * from movielist1")

user = mycursor.fetchall()

for i in user:
    print(i)