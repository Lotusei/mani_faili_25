# import sqlite3

# # Connect to SQLite and create a database file
# conn = sqlite3.connect('restorani_riga.db')

# # Create a cursor object using the connection
# cursor = conn.cursor()

# mazak = cursor.execute("SELECT COUNT (id) FROM restorani WHERE novērtējums < 4.0")
# print(f'Izdzēsti {mazak} ieraksti')
# cursor.execute("DELETE FROM restorani WHERE novērtējums < 4.0")

# # Fetch and print the results

# results = cursor.fetchall()
# print('Restorāni ar novērtējumu < 4.0 (tiks dzēsti):')
# for row in results:
#     print(row)

# palika = cursor.execute("SELECT COUNT (*) FROM restorani")
# print(f'Datu bāzē palikuši: {palika} restorāni')
# conn.commit()