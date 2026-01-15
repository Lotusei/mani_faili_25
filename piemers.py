# import datetime

# while True:
#   print("Izvēlne:")
#   print("1. Parādīt sveicienu")
#   print("2. Parādīt datumu")
#   print("3. Parādīt laiku")
#   print("4. Iziet")

#   izvēle = input("Ievadiet savu izvēli (1-4): ")

#   if izvēle == '1':
#     print("Sveiki! Šī ir Python izvēlnes programma.")
#   elif izvēle == '2':
#     šodien = datetime.date.today()
#     print(f"Šodien ir {šodien}")
#   elif izvēle == '3':
#     tagad = datetime.datetime.now().time()
#     print(f"Pašreizējais laiks ir {tagad}")
#   elif izvēle == '4':
#     print("Paldies par programmas izmantošanu!")
#     break
#   else:
#     print("Nepareiza izvēle. Lūdzu, ievadiet skaitli no 1 līdz 4.")

# -------------------------------------------------------------------------------------------------

# def parādīt_sveicienu():
#   """Izvada sveiciena tekstu."""
#   print("Sveiki! Šī ir Python izvēlnes programma.")

# def parādīt_datumu():
#   """Izvada šodienas datumu."""
#   import datetime
#   šodien = datetime.date.today()
#   print(f"Šodien ir {šodien}")

# def parādīt_laiku():
#   """Izvada pašreizējo laiku."""
#   import datetime
#   tagad = datetime.datetime.now().time()
#   print(f"Pašreizējais laiks ir {tagad}")

# while True:
#   print("Izvēlne:")
#   print("1. Parādīt sveicienu")
#   print("2. Parādīt datumu")
#   print("3. Parādīt laiku")
#   print("4. Iziet")

#   izvēle = input("Ievadiet savu izvēli (1-4): ")

#   if izvēle == '1':
#     parādīt_sveicienu()
#   elif izvēle == '2':
#     parādīt_datumu()
#   elif izvēle == '3':
#     parādīt_laiku()
#   elif izvēle == '4':
#     print("Paldies par programmas izmantošanu!")
#     break
#   else:
#     print("Nepareiza izvēle. Lūdzu, ievadiet skaitli no 1 līdz 4.")