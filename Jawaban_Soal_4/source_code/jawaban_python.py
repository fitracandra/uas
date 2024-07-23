#contoh menggnunakan sqlite3
import sqlite3

# Connect to database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# Insert a row of data
c.execute("INSERT INTO users (name) VALUES ('Alice')")

# Commit the changes
conn.commit()

# Retrieve data
c.execute('SELECT * FROM users')
print(c.fetchall())

# Close the connection
conn.close()
