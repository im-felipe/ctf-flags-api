import sqlite3

conexion = sqlite3.connect("flags.db")
cursor = conexion.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS flags(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reto TEXT NOT NULL,
        flag_hash_o_texto TEXT NOT NULL,
        puntos INTEGER,
        resuelta INTEGER NOT NULL DEFAULT 0
    )
"""
)

conexion.commit()
conexion.close()