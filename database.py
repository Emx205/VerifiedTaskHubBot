import sqlite3

DB_NAME = "verifiedtaskhub.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        balance INTEGER DEFAULT 0,
        referrals INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS submissions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        status TEXT DEFAULT 'Pending'
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS withdrawals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        account_name TEXT,
        account_number TEXT,
        bank_name TEXT,
        amount INTEGER,
        status TEXT DEFAULT 'Pending'
    )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, username, first_name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users(user_id, username, first_name)
    VALUES(?,?,?)
    """, (user_id, username, first_name))

    conn.commit()
    conn.close()


def get_balance(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    return 0


def update_balance(user_id, amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET balance = balance + ?
    WHERE user_id=?
    """, (amount, user_id))

    conn.commit()
    conn.close()
