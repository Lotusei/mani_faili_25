# try:
#     with open("dati.txt", "r") as fails:
# # A. Lasīt visu saturu kā vienu virkni
#         viss_saturs = fails.read()
#         print("\n--- A. Viss Saturs ---")
#         print(viss_saturs)

# except FileNotFoundError:
#     print("Fails 'dati.txt' nav atrasts. Lūdzu, izveidojiet to.")

# Uzd.1 ------------------------------------------------------------------------------------------------------------

# with open('Teksts.txt', 'r', encoding='utf-8') as f:
#     saturs = f.read()
#     print(saturs.upper())
#     # Further file processing goes here

# Uzd. 2 ------------------------------------------------------------------------------------------------------------

vards = input("Ievadi savu vārdu: ")
vecums = input("Ievadi savu vecumu: ")

with open("Teksts2.txt", "a", encoding = 'utf-8') as f:
  f.write(f"{vards},{vecums}\n")

print("Dati saglabāti!")

with open("Teksts2.txt") as f:
  print(f.read())