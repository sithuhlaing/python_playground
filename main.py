#!/usr/bin/python
import requests
import cgitb
import sys
import argparse
import urllib
import cgi
import json
import mysql.connector
from mysql.connector import errorcode

cgitb.enable()
print "Content-type:text/html\n"
print ("okkar")

#Connection DB
mydb = mysql.connector.connect(
    host="localhost",
    user="",
    passwd="",
    database="mydatabase"
)

#mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE inventory ( name varchar(8), amount int(255), price int(255))")
#sql = "DROP TABLE inventory"
#mycursor.execute(sql)

arguments = cgi.FieldStorage()
if arguments['function'].value =="addstock":
   name =(arguments['name'].value)
   print("name :" + name)
   amount =(arguments['amount'].value)
   print("amount :"+ amount)
   cursor.execute('insert into inventory(name, amount) values (%s, %n)', (name, amount)
   mydb.commit()
   #if arguments['function'].value =="deleteall":
   #   print("delete")
    #        print("deleteall :" + arguments['name'].value.replace(" ", "+"))
           # mycursor.execute('delete from inventory')
    #if i == "sell":
    #      print("sell :" + arguments['name'].value.replace(" ", "+"))
           # name = arguments['name'].value
           # amount = arguments['amount'].value
           # cursor.execute('')
    #if i == "checkstock":
    #       print("checkstock :" + arguments['name'].value.replace(" ", "+"))
           # name = arguments['name'].value
           # cursor.execute('select sum(amount) from inventory where name = %s', name)
       #except NameError:
       # print("execptNameError")
#else:
   #print("error :" + arguments['name'].value.replace(" ", "+"))
#   print("ERROR")

#mydb.commit()
print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM inventory")
myresult = mycursor.fetchall()
for x in myresult:
   print(x)