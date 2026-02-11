# import sqlite3

# # Connect to SQLite and create a database file
# conn = sqlite3.connect('restorani_riga.db')

# # Create a cursor object using the connection
# cursor = conn.cursor()

# cursor.execute("SELECT nosaukums, virtuve, videja_cena FROM restorani WHERE videja_cena BETWEEN 15 and 30")

# # Fetch and print the results
# count = 0
# results = cursor.fetchall()
# print('Restorāni ar vidējo cenu 15-30 EUR:')
# for row in results:
#     count += 1
#     print(row)
# print(f'Kopā atrasts: {count} restorāni')

# conn.commit()