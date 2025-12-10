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

# with open('dati2.csv','a', newline='', encoding='utf-8') as f:
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

# 2. uzd 10.12.2025 --------------------------------------------------------------------------------------------------------------------------

