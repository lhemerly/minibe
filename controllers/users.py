import sqlite3
from models.user import User, UserInDB


def get_db():
    return sqlite3.connect("db.sqlite3")


def parse_user(row: tuple) -> UserInDB:
    """Parse a database row into a UserInDB instance."""
    if row is None:
        return None
    return UserInDB(
        username=row[1],
        email=row[2],
        full_name=row[3],
        hashed_password=row[4],
        disabled=row[5],
        verified=row[6],
    )


async def get_user(username: str) -> UserInDB:
    """Retrieve a user by username."""
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return parse_user(cursor.fetchone())


async def get_user_by_email(email: str) -> UserInDB:
    """Retrieve a user by email."""
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return parse_user(cursor.fetchone())


async def get_user_by_full_name(full_name: str) -> UserInDB:
    """Retrieve a user by full name."""
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE full_name = ?", (full_name,))
        return parse_user(cursor.fetchone())


async def create_user(user: UserInDB) -> User:
    """Create a new user and return the created user."""
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute(
            """
            INSERT INTO users (username, email, full_name, hashed_password, disabled, verified)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                user.username,
                user.email,
                user.full_name,
                user.hashed_password,
                user.verified,
                user.disabled,
            ),
        )
        db.commit()
        return user


async def delete_user(username: str) -> None:
    """Delete a user by username."""
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        db.commit()
