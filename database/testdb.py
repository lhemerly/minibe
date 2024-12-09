import sqlite3

with sqlite3.connect("db.sqlite3") as db:
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT * FROM users;
        """
    )
    print(cursor.fetchall())
