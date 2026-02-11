import sqlite3

# Connect to SQLite and create a database file
conn = sqlite3.connect('restorani_riga.db')

# Create a cursor object using the connection
cursor = conn.cursor()

cursor.execute("SELECT nosaukums, virtuve FROM restorani WHERE nosaukums LIKE '%C%'")

# Fetch and print the results

results = cursor.fetchall()
print('Restorāni ar "C" nosaukumā:')
for row in results:
    print(row)

#------------------------------------------------------------------------------
cursor.execute("SELECT nosaukums, novērtējums FROM restorani WHERE virtuve LIKE 'Itāļu'")

# Fetch and print the results

results = cursor.fetchall()
print('Restorāni ar Itāļu virtuvi:')
for row in results:
    print(row)

#------------------------------------------------------------------------------
cursor.execute("SELECT nosaukums FROM restorani WHERE virtuve LIKE '_iro_a_'")

# Fetch and print the results

results = cursor.fetchall()
print('Restorāni ar Eiropas virtuvi:')
for row in results:
    print(row)


conn.commit()