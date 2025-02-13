import sqlite3
from config import DATABASE_NAME

def connect():
    return sqlite3.connect(DATABASE_NAME)

def create_table():
    conn = connect()
    cursor =conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS buku (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   judul TEXT NOT NULL,
                   penulis TEXT NOT NULL,
                   tahun INTEGER NOT NULL,
                   status TEXT DEFAULT 'tersedia'
                )
        """)
    conn.commit() # Menyimpan perubahan
    conn.close() # Menutup Database

create_table()
