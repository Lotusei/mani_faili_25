# import sqlite3

# # Connect to SQLite and create a database file
# conn = sqlite3.connect('restorani_riga.db')

# # Create a cursor object using the connection
# cursor = conn.cursor()

# cursor.execute("SELECT nosaukums, virtuve, novērtējums FROM restorani WHERE novērtējums >= 4.5")

# # Fetch and print the results
# count = 0
# results = cursor.fetchall()
# print('Restorāni ar novērtējumu >= 4.5:')
# for row in results:
#     count += 1
#     print(row)
# print(f'Kopā atrasts: {count} restorāni')

# conn.commit()