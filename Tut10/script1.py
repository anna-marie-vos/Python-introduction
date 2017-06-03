# sqlite is a "portable database" for small databases
# its a built-in library in python.

# this program will connect to a database
# Create a cursor object
# write an SQL query
# commit changes to database

import sqlite3 as db

def createTable():
    conn = db.connect("lite.db") #this will create the database if you dont already have one
    cur = conn.cursor() #this creates the cursor
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #write straightup SQL
    conn.commit() # commit changes
    conn.close() #close connection

def insertData(item, quantity, price):
    conn = db.connect("lite.db")
    cur = conn.cursor()
    # add data to store
    # add ? to avoid SQL injections
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit() # commit changes
    conn.close() #close connection

# insertData('water glas', 10, 5.5)
# insertData('Coffee Cup', 20, 9)

def viewDataBase():
    conn = db.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def deleteRow(deletedItem):
    conn = db.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (deletedItem,)) #dont forget the comma
    conn.commit()
    conn.close()

# deleteRow("Wine Glass")

def updateRow(updatedItem, newAmount, newPrice):
    conn = db.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", ( newAmount, newPrice, updatedItem)) #dont forget the comma
    conn.commit()
    conn.close()

updateRow('water glas', 15, 10)

print(viewDataBase())
