import csv

# Uzdevums 04.12.25. -----------------------------------------------------------------------------------------------------


# with open('dati.csv',encoding='utf-8') as f:
#     lasītājs = csv.reader(f)
    # next (lasītājs)
    # for rinda in lasītājs:
    #     print(rinda[0], rinda[1], rinda[2], int(rinda[3]))

# otrais.1  ------------------------------------------------------------------------------------------------------------------

# with open('dati.csv',encoding='utf-8') as f:
#     lasītājs = csv.reader(f)
#     print("Skolēni ar vairāk nekā 80 punktiem:")
#     next (lasītājs)
#     for rinda in lasītājs:
#         if int(rinda[3]) > 80:
#             print(rinda[1], int(rinda[3]))
#         else:
#             pass

# otrais.2 --------------------------------------------------------------------------------------------------------------



# kaut kas cits ---------------------------------------------------------------------------------------------------------

# vards = input("Vārds: ").capitalize()
# uzvards = input("Uzvārds ").capitalize()
# klase = input("Klase: ").upper()

# with open('skoleni.csv','a', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     if f.tell() == 0:
#         writer.writerow(['Vārds', 'Uzvārds', 'Klase'])
#     writer.writerow([vards, uzvards, klase])
# print("Saglabāts!")

# 1. uzd 10.12.2025 --------------------------------------------------------------------------------------------------------------------------


# with open('dati2.csv','a', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     if f.tell() == 0:
#         writer.writerow(['Vārds', 'Uzvārds', 'Klase'])
#     while True:
#         vards = input("Vārds: ").strip().capitalize()

#         if vards == "":
#             print('\nReģistrācija pabeigta')
#             break

#         uzvards = input("Uzvārds ").strip().capitalize()
#         klase = input("Klase: ").strip().upper()

#         writer.writerow([vards, uzvards, klase])

# print("Saglabāts!")

# 1. uzd savādāks 10.12.2025 --------------------------------------------------------------------------------------------------------------------------

# # Dati tiek pievienoti skoleni.csv failam.
# # Pēc ievades programma nolasīs failu un pieprasa klasi un
# # atlasa/izdrukā tikai pieprasītās klases skolēnus, izvada atlasītos datus jaunā csv failā

# import csv

# print("=== Skolēnu reģistrācija ===")
# print("Ievadi skolēnus. Lai beigtu — atstāj 'Vārds' lauku tukšu un spied Enter.\n")

# # 1. Ievade un saglabāšana failā skoleni.csv
# with open('skoleni.csv', 'a', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
    
#     # Ja fails tukšs — pievienojam virsrakstus
#     if f.tell() == 0:
#         writer.writerow(['Vārds', 'Uzvārds', 'Klase'])

#     while True:
#         vards = input("Vārds: ").strip()
#         if vards == "":                    # tukšs vārds = beigt ievadi
#             print("Ievade pabeigta!\n")
#             break
#         uzvards = input("Uzvārds: ").strip().capitalize()
#         klase = input("Klase (piem. 10.A): ").strip().upper()

#         # Saglabājam CSV failā
#         writer.writerow([vards.capitalize(), uzvards, klase])
#         print(f"Pievienots: {vards.capitalize()} {uzvards} no {klase} klases\n")

# 2. uzd savādāks 10.12.2025 --------------------------------------------------------------------------------------------------------------------------

# # Nolasām visus datus no faila
# while True:
#     skoleni = []

#     with open('skoleni.csv', 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         next(reader)  # izlaižam virsrakstus (Vārds,Uzvārds,Klase)

#         for rinda in reader:
#             if len(rinda) != 0:           # ja rinda nav tukša
#                 skoleni.append(rinda)
#         # Ja nav datu
#         if len(skoleni) == 0:
#             print("Failā nav skolēnu. Pievieno vismaz vienu!")
#             break
            
            
        
#         mekle_klase = input("\nKuras klases skolēnus gribi redzēt? (piem. 8. - 12. A/B): ").strip().upper()

#         atrastie = []
#         for skolens in skoleni:
#             if skolens[2] == mekle_klase:
#                 atrastie.append(skolens)

#         if len(atrastie) > 0:
#             print(f"\nSkolēni no {mekle_klase} klases:")
#     #         print (atrastie)
#             for s in atrastie:
#                 print(f"• {s[0]} {s[1]}")
                
#         break

# # Eksportējam uz atsevišķu failu
# faila_nosaukums = mekle_klase + "_klase.csv"
# with open(faila_nosaukums, 'w', newline='', encoding='utf-8') as eks:
#     writer = csv.writer(eks)
#     writer.writerow(['Vārds', 'Uzvārds', 'Klase'])
#     for s in atrastie:
#         writer.writerow(s)

#     print(f"\nSaglabāts failā: {faila_nosaukums}")