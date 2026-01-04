import sqlite3


def get_db_conn(name="db.sqlite3"):
    conn = sqlite3.connect(name)
    return conn


def close_db_conn(conn):
    conn.close()
    return


def init_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS test (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       text TEXT NOT NULL
                   )
    """)
    conn.commit()
    return


def insert_test_data(conn, text):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO test (text) VALUES (?)", (text,))
    conn.commit()
    return


def fetch_all_test_data(conn):
    """
    Returns:
        list[list[tuple]]: [(id, text), ...]
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test")
    return cursor.fetchall()


def fetch_test(conn, id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test WHERE id = ?", (id,))
    return cursor.fetchone()


def delete_test_data(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM test WHERE id = ?", (id,))
    conn.commit()
    return
