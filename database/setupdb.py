import sqlite3

db = sqlite3.connect("db.sqlite3")

# create users table
db.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        full_name TEXT NOT NULL,
        hashed_password TEXT NOT NULL,
        verified BOOLEAN DEFAULT FALSE,
        disabled BOOLEAN DEFAULT FALSE
    )
    """
)
