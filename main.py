import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="vageesh", passwd="1964", port="3306", database="movielist")

mycursor = mydb.cursor()

#Insertion to DB
sqlform = "Insert into movielist1(name,actor,actress,director,yearofrelease) values(%s,%s,%s,%s,%s)"

movielist1 = [("vajrakaya","Shivraj","Nabha","Harsha","2016"),("KGF","yash","Srinidhi","Prashanth","2018")]

mycursor.executemany(sqlform,movielist1)

mydb.commit()

mycursor.execute("select * from movielist1")

user = mycursor.fetchall()

for i in user:
    print(i)