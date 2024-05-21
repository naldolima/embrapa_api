import sqlite3

# filename to form database
file = "embrapa.db"

try:
    conn = sqlite3.connect(file)
    print(f"Database {file} formed.")
except:
    print(f"Database {file} not formed.")

