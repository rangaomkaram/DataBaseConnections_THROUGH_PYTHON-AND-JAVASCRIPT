"""
1. Connect the MySql using Python
2. Retrive the Data from Database from MySQL  
3. Do Some Operation and Manpulations on Data.

"""

####################################################################
"""
GET CONNECTED WITH MYSQL
"""
###################################################################

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Ranga",
  password="Ranga@1993!",
  database = "ROYAL_BANK_AUS"
)

mycursor = mydb.cursor()
"""mycursor.execute('SELECT * FROM ACCT_BASE LIMIT 7')


"""
mycursor.execute('SHOW COLUMNS FROM ACCT_BASE')

print(mydb)
for table in mycursor:
    print(table)