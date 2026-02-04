import sqlite3

# Connect to SQLite and create a database file
conn = sqlite3.connect('FriendList.db')

# Create a cursor object using the connection
cursor = conn.cursor()

# Create a new table named 'friends' /nevar būt vienlaicīgi ar otru/ "add a friend"
# cursor.execute('''
#     CREATE TABLE friends (
#         name TEXT,
#         age INTEGER,
#         hobby TEXT,
#         phone TEXT
#     )
# ''')

# Add a friend's information
# cursor.execute('''INSERT INTO friends (name, age, hobby, phone) VALUES ('Alice', 16, 'Reading', '123-456-7890')''')
# cursor.execute('''INSERT INTO friends (name, age, hobby, phone) VALUES ('Bob', 23, 'Cycling', '555-0102')''')
# cursor.execute('''INSERT INTO friends (name, age, hobby, phone) VALUES ('Emily', 29, 'Painting', '555-0103')''')
# cursor.execute('''INSERT INTO friends (name, age, hobby, phone) VALUES ('Charlie', 20, 'Hiking', '555-0110')''')
# Save (commit) the changes
conn.commit()

# Connect to your database
conn = sqlite3.connect('FriendList.db')
cursor = conn.cursor()

# SQL query to find friends who are 25 years old
cursor.execute("SELECT * FROM friends WHERE age = 29")

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

cursor.execute("SELECT * FROM friends ORDER BY name")
# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Create an index for the 'name' column in the 'friends' table
cursor.execute("CREATE INDEX idx_name ON friends (name)")

# Close the connection to the database
conn.close()

