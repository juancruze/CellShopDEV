import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('registro.db')

conn.execute('''
    CREATE TABLE register (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        confirm_password TEXT NOT NULL
''')

# Cerrar la conexión a la base de datos
conn.close()

print("Base de datos inicializada correctamente.")


