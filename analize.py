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

vards = input("Ievadi savu vārdu: ")
uzvards = input("Ievadi savu uzvardu: ")
klase = input("Ievadi savu klasi (ciparu): ")

with open('dati2.csv','w', newline='') as f:
    rakstītājs = csv.writer(f)
    rakstītājs.writerow([vards,uzvards,klase])
