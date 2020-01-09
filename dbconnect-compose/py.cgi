#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb
import os
#mysql database connectivity

import mysql.connector

mydb = mysql.connector.connect(
  host=os.environ['MYSQL_HOST'],
  user="root",
  passwd="akash123",
  database="users"
)

mycursor = mydb.cursor()
mycursor.execute("select * from login")
myresult = mycursor.fetchall() # it gives the list

# Create instance of FieldStorage
print ("Content-type: text/html\n")

form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('Username')
password  = form.getvalue('Password')


for row in myresult:
        if (username == row[0]) and (password == row[1]):
                print("content-type:text/html\n")
                print("welcome")

        else:
                print("Content-type:text/html\n")
                print("<h2>Username and Password Incorrect</h2>")


mycursor.close()
