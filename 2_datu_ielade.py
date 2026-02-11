# import sqlite3

# # Connect to SQLite and create a database file
# conn = sqlite3.connect('restorani_riga.db')

# # Create a cursor object using the connection
# cursor = conn.cursor()

# # Latvijas restorāni Rīgā
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Vincents', 'Eiropas', 4.8, 45)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('3 Pavāru', 'Latviešu', 4.7, 40)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Riits', 'Latviešu', 4.6, 35)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Bibliotēka No1', 'Eiropas', 4.5, 38)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Charlestons', 'Amerikāņu', 4.4, 32)''');

# #Itāļu restorāni
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Mio', 'Itāļu', 4.6, 28)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Trattoria Robertino', 'Itāļu', 4.7, 30)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Picas Lulū', 'Itāļu', 4.3, 18)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Il Patio', 'Itāļu', 4.5, 25)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Da Sergio', 'Itāļu', 4.8, 35)''');

# #Āzijas virtuve
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Monsoon', 'Indiešu', 4.4, 22)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Sushi City', 'Japāņu', 4.2, 20)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Cili Pica', 'Āzijas', 4.1, 15)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Rama', 'Taju', 4.5, 18)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Lucky Dragon', 'Ķīniešu', 4.3, 16)''');

# #Fast food un casual dining
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Lido', 'Latviešu', 4.0, 12)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Čili Pizza', 'Itāļu', 3.9, 14)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Hesburger', 'Fast food', 3.7, 8)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('McDonald''s', 'Fast food', 3.6, 9)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('KFC', 'Fast food', 3.8, 10)''');

# #Kafejnīcas un brunch vietas
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Miit Coffee', 'Kafejnīca', 4.6, 12)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Double Coffee', 'Kafejnīca', 4.2, 10)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Rocket Bean Roastery', 'Kafejnīca', 4.7, 11)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Ezītis miglā', 'Kafejnīca', 4.5, 13)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Café Osiris', 'Kafejnīca', 4.4, 14)''');

# #Steikhausas un grili
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Steiku Haoss', 'Amerikāņu', 4.5, 35)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Texas Honky Tonk', 'Amerikāņu', 4.3, 28)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Black Magic', 'Amerikāņu', 4.6, 32)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Čārlstonas grils', 'Amerikāņu', 4.4, 30)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('BBQ House', 'Amerikāņu', 4.2, 25)''');

# #Veģetārieši un veselīga pārtika
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Vairāk saules', 'Veģetārā', 4.5, 16)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Raw Garden', 'Veģetārā', 4.6, 18)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Veggies', 'Veģetārā', 4.3, 14)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Terapija', 'Veselīga', 4.4, 15)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Green Cafe', 'Veselīga', 4.2, 13)''');

# #Ekskluzīvi un gourmet
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Entresol', 'Franču', 4.9, 55)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Restaurant 1221', 'Eiropas', 4.8, 50)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Ferma', 'Latviešu', 4.7, 42)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Forest', 'Skandināvu', 4.6, 48)''');
# cursor.execute('''INSERT INTO restorani (nosaukums, virtuve, novērtējums, videja_cena) VALUES ('Stage 22', 'Eiropas', 4.5, 40)''');


# conn.commit()