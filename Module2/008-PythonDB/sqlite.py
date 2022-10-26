# sqlite is a local dev sql database, that is only active when the python app is running
# The data does not persist, but uses same functionality of data

import sqlite3 as sqlite

conn = sqlite.connect("test-db")

cursor = conn.cursor()

sql_file = open("students.sql")
sql_string = sql_file.read()
cursor.executescript(sql_string)

print(cursor.execute("SELECT * FROM students").fetchall())