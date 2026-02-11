# import sqlite3

# # Connect to SQLite and create a database file
# conn = sqlite3.connect('restorani_riga.db')

# # Create a cursor object using the connection
# cursor = conn.cursor()

# # Create a new table named 'friends' /nevar būt vienlaicīgi ar otru/ "add a friend"
# cursor.execute('''
#     CREATE TABLE restorani (
#         id INTEGER PRIMARY KEY,
#         nosaukums TEXT NOT NULL,
#         virtuve TEXT NOT NULL,
#         novērtējums REAL,
#         videja_cena INTEGER
#     )
# ''')

# conn.commit()