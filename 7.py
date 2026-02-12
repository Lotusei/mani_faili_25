# import sqlite3

# # Connect to SQLite and create a database file
# conn = sqlite3.connect('restorani_riga.db')

# # Create a cursor object using the connection
# cursor = conn.cursor()

# print(f'Pirms izmaiņām:\n (Vincents, Eiropas, 45)')

# cursor.execute("UPDATE restorani SET videja_cena = 50 WHERE id = 1")
# # Fetch and print the results

# print(f'Pēc izmaiņām:\n (Vincents, Eiropas, 50)')

# conn.commit()