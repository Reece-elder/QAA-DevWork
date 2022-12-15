import sqlite3

conn = sqlite3.connect("new-db")

cursor = conn.cursor()

# cursor.execute("CREATE TABLE birds(colour, flight, name)")

# data = cursor.execute("SELECT name from sqlite_master")
# print(data.fetchone())

cursor.execute("""
    INSERT INTO birds VALUES('Purple',TRUE, 'Polly')
""")

conn.commit()
data = cursor.execute("SELECT * FROM birds")
print(data.fetchall())