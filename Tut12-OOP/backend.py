import sqlite3 as db

    def connect():
        conn = db.connect("books.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()

    def insert(title, author, year, isbn):
        conn = db.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES(null, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view():
        conn = db.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(title="", author="", year="", isbn=""):
        conn = db.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(id):
        conn = db.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def update(id,title, author, year, isbn):
        conn = db.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?,year=?,isbn=? WHERE id = ?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()

    connect()
# insert("The air","Jane Smith",1925, 5523232)
# print(search(author ="John Smith"))
# delete(4)
# update(3, "The Moon", "Jon Joe", 11232, 122233333)
# print(view())
