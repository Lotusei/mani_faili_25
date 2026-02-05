import sqlite3

# Connect to SQLite and create a database file
conn = sqlite3.connect('auto_tirgus.db')

# Create a cursor object using the connection
cursor = conn.cursor()

# Create a new table named 'friends' /nevar būt vienlaicīgi ar otru/ "add a friend"
# cursor.execute('''
#     CREATE TABLE auto (
#         id INTEGER PRIMARY KEY,
#         Marka TEXT NOT NULL,
#         Modelis TEXT NOT NULL,
#         gads INTEGER,
#         nobraukums INTEGER
#     )
# ''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Audi', 'A4', 2018, 120000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('BMW', '320i', 2020, 50000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Volkswagen', 'Golf', 2015, 180000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Toyota', 'Corolla', 2022, 25000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Mercedes-Benz', 'C-Class', 2019, 90000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Audi', 'A6', 2021, 45000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Audi', 'Q5', 2017, 135000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('BMW', 'X5', 2019, 78000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('BMW', '530d', 2023, 15000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Mercedes-Benz', 'E-Class', 2020, 62000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Mercedes-Benz', 'GLC', 2018, 95000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Volkswagen', 'Passat', 2016, 145000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Volkswagen', 'Tiguan', 2021, 38000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Toyota', 'RAV4', 2020, 55000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Toyota', 'Camry', 2019, 72000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Toyota', 'Yaris', 2023, 8000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Honda', 'Civic', 2018, 98000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Honda', 'Accord', 2020, 65000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Honda', 'CR-V', 2022, 28000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Mazda', 'CX-5', 2019, 83000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Mazda', '6', 2017, 115000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Mazda', '3', 2021, 42000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Ford', 'Focus', 2016, 156000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Ford', 'Fiesta', 2015, 172000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Ford', 'Mondeo', 2018, 105000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Nissan', 'Qashqai', 2020, 58000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Nissan', 'Juke', 2019, 75000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Nissan', 'X-Trail', 2021, 35000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Hyundai', 'Tucson', 2022, 22000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Hyundai', 'i30', 2019, 88000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Hyundai', 'Kona', 2023, 5000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Kia', 'Sportage', 2020, 67000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Kia', 'Ceed', 2018, 102000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Kia', 'Sorento', 2021, 44000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Skoda', 'Octavia', 2019, 79000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Skoda', 'Superb', 2020, 61000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Skoda', 'Karoq', 2022, 18000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Volvo', 'XC60', 2019, 85000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Volvo', 'S60', 2021, 39000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Volvo', 'V90', 2018, 110000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Peugeot', '308', 2017, 128000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Peugeot', '3008', 2020, 54000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Peugeot', '208', 2022, 31000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Renault', 'Clio', 2016, 148000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Renault', 'Megane', 2019, 92000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Renault', 'Captur', 2021, 47000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Opel', 'Astra', 2018, 112000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Opel', 'Insignia', 2017, 138000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Opel', 'Corsa', 2020, 63000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Seat', 'Leon', 2019, 81000)''')

# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Seat', 'Ateca', 2021, 36000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Seat', 'Ibiza', 2016, 159000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Subaru', 'Outback', 2020, 71000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Subaru', 'Forester', 2022, 19000)''')
# cursor.execute('''INSERT INTO auto (Marka, Modelis, gads, nobraukums) VALUES ('Lexus', 'IS', 2019, 56000)''')



cursor.execute("SELECT * FROM auto WHERE gads = 2020")

# Fetch and print the results
count = 0
results = cursor.fetchall()
print('Automašīnas, kas izlaistas 2020. gadā:')
for row in results:
    count += 1
    print(row)
print(f'Kopā atrasts: {count} automašīnas')


cursor.execute("SELECT * FROM auto WHERE nobraukums BETWEEN 50000 AND 100000")

# Fetch and print the results
count = 0
results = cursor.fetchall()
print('Automašīnas ar nobraukumu 50000-100000 km:')
for row in results:
    count += 1
    print(row)
print(f'Kopā atrasts: {count} automašīnas')




# Add a auto's information
# cursor.execute('''INSERT INTO friends (id, Marka, Modelis, gads, nobraukums) VALUES ('Alice', 16, 'Reading', '123-456-7890')''')

# # Save (commit) the changes
conn.commit()