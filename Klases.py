# class Ingridients:
#     def __init__ (self, name, weight):
#         self.name = name
#         self.weight = weight

# pot = Ingridients("Carrot", "2kg")

# print(pot.name)
# print(pot.weight)

# ---------------------------------------------------------------------------------------------------------------

# class Persona:
#     def __init__(self, vards, uzvards):
#         self.vards = vards
#         self.uzvards = uzvards
#     def pilnsVards(self):
#         print(self.vards + " " + self.uzvards)


# P1 = Persona("Perrijs", "Platapus")

# print(P1.vards)
# print(P1.uzvards)

# P1.pilnsVards()

# ---------------------------------------------------------------------------------------------------------------------------

# import math
# class Rinkis:
#     def __init__(self, radiuss, vards):
#         self.radiuss = radiuss
#         self.vards = vards
#     def RinkaLaukums(self):
#         # return math.pi * self.radiuss ** 2
#         print("Rinķia " + self. vards + " laukums ir" , math.pi*self.radiuss**2 , "kvadrātcentimetrus liels.")
#     def RinkaLinija(self):
#         # return 2 * math.pi * self.radiuss ** 2
#         print("Rinķia "+ self. vards + " līnija ir" , 2*math.pi*self.radiuss**2 , "centimetrus gara.")


# R = Rinkis(16, "A")

# print(R.radiuss)
# print(R.vards)

# R.RinkaLinija()
# R.RinkaLaukums()

# -------------------------------------------------------------------------------------------------------------------------------------------

from datetime import date

class Persona:
    def __init__(self, vards, valsts, dzgads):
        self.vards = vards
        self.valsts = valsts
        self.dzgads = dzgads
    def vecums(self):
        print(self.vards + " no " + self.valsts + "s ir" , date.today().year - self.dzgads.year , "gadus vecs/a.")


P1 = Persona("Perrijs", "Krievija", date(1638, 12, 25))

print(P1.vards)
print(P1.valsts)
print(P1.dzgads)

P1.vecums()