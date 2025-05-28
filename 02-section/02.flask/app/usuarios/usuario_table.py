import sqlite3

class SQLiteTable:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo TEXT,
            alias TEXT,
            password TEXT,
            fecha_registro DATE
        )'''
        )

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
