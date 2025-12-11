# import csv


# print("=== Pirkumu reģistrācija ===")
# print("Ievadi pirkumus. Lai beigtu — atstāj 'Produkts' lauku tukšu un spied Enter.\n")

# # 1. Ievade un saglabāšana failā skoleni.csv
# with open('ceks.csv', 'a', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
    
#     # Ja fails tukšs — pievienojam virsrakstus
#     if f.tell() == 0:
#         writer.writerow(['Produkts', 'Cena'])

#     while True:
#         produkts = input("Produkts: ").strip().capitalize()
#         if produkts == "":
#             print("Ievade pabeigta!\n")
#             break
#         cena = input("Cena (raksti ar punktu): ").strip()

#         # Saglabājam CSV failā
#         writer.writerow([produkts, cena])
#         print(f"Pievienots: {produkts} kurš maksā {cena} eiro.\n")

# 2. daļa ----------------------------------------------------------

# Nolasām visus datus no faila
while True:
    produkti = []

    with open('ceks.txt', 'r', encoding='utf-8') as f:
        reader = f.read
        next(reader)  # izlaižam virsrakstus (Vārds,Uzvārds,Klase)

        for rinda in reader:
            if len(rinda) != 0:           # ja rinda nav tukša
                produkti.append(rinda)
        # Ja nav datu
        if len(produkti) == 0:
            print("Failā nav produktu. Pievieno vismaz vienu!")
            break
            
            
# nezinu ------------------- zem
        atrastie = []
        for produkts in produkti:

        if len(atrastie) > 0:
            print(f"\n=============================================")
    #         print (atrastie)
            for s in atrastie:
                print(f"• {s[0]} {s[1]}")
                
        break

# Eksportējam uz atsevišķu failu
faila_nosaukums = "ceks.txt"
with open(faila_nosaukums, 'w', newline='', encoding='utf-8') as teksts:
    writer = teksts.write
    writer.writelines(['Vārds', 'Uzvārds', 'Klase'])
    for s in atrastie:
        writer.writelines(s)

    print(f"\nSaglabāts failā: {faila_nosaukums}")