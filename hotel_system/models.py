import sqlite3

def get_db():
    conn = sqlite3.connect('hotel.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY,
            number TEXT,
            type TEXT,
            price REAL,
            status TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT,
            email TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY,
            room_id INTEGER,
            guest_id INTEGER,
            check_in TEXT,
            check_out TEXT,
            FOREIGN KEY(room_id) REFERENCES rooms(id),
            FOREIGN KEY(guest_id) REFERENCES guests(id)
        )
    ''')
    conn.commit()
    conn.close()
