import sqlite3

def init_db():
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            room_number TEXT NOT NULL,
            check_in DATE,
            check_out DATE
        )
    """)
    conn.commit()
    conn.close()
