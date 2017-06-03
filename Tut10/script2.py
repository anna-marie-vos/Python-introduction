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
    conn = db.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()
