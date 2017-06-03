# postgress = psycopg2
# create a database in the terminal: tutorialdb
import psycopg2 as db

def createTable():
    conn = db.connect("dbname = 'tutorialdb' user='postgres' password='postgres' host='localhost' port=5432")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

createTable()

def insertData(item, quantity, price):
    conn = db.connect("dbname = 'tutorialdb' user='postgres' password='postgres' host='localhost' port=5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

# insertData('mango', 18, 4.5)

def viewDataBase():
    conn = db.connect("dbname = 'tutorialdb' user='postgres' password='postgres' host='localhost' port=5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def deleteRow(deletedItem):
    conn = db.connect("dbname = 'tutorialdb' user='postgres' password='postgres' host='localhost' port=5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (deletedItem,))
    conn.commit()
    conn.close()

# deleteRow('mango')

def updateRow(updatedItem, newAmount, newPrice):
    conn = db.connect("dbname = 'tutorialdb' user='postgres' password='postgres' host='localhost' port=5432")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", ( newAmount, newPrice, updatedItem))
    conn.commit()
    conn.close()

updateRow('orange', 100, 4)

print(viewDataBase())
