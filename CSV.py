import csv

# with open('students0.csv','r') as fails:
#     lasītājs = csv.reader(fails)
#     for rinda in lasītājs:
#         print(f"{rinda[0]} is in {rinda[1]}")

# parastais ---------------------------------------------

# with open('cilveki.csv',encoding='utf-8') as f:
#     lasītājs = csv.reader(f)
#     next (lasītājs)
#     for rinda in lasītājs:
#         print(rinda[0], rinda[1])

# dictionary reader ------------------------------------------------

# with open('cilveki.csv',encoding='utf-8') as f:
#     lasītājs = csv.DictReader(f)
#     next (lasītājs)
#     for rinda in lasītājs:
#         print(rinda['vards'], rinda['uzvards'])

# ----------------------------------------------------------

summa = 0
skaits = 0
with open('cilveki.csv',encoding='utf-8') as f:
    lasītājs = csv.DictReader(f)
    next (lasītājs)
    for rinda in lasītājs:
        summa += int(rinda['vecums'])
        skaits += 1
    vid = summa / skaits
    print(f"Vidējais vecums ir: {vid} gadi")
