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

# from datetime import date

# class Persona:
#     def __init__(self, vards, valsts, dzgads):
#         self.vards = vards
#         self.valsts = valsts
#         self.dzgads = dzgads
#     def vecums(self):
#         print(self.vards + " no " + self.valsts + "s ir" , date.today().year - self.dzgads.year , "gadus vecs/a.")


# P1 = Persona("Perrijs", "Krievija", date(1638, 12, 25))

# print(P1.vards)
# print(P1.valsts)
# print(P1.dzgads)

# P1.vecums()

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self, vards, atzime, atzime1):
#         self.vards = vards
#         self.atzime = atzime
#         self.atzime1 = atzime1

#     def avarage_grade(self):
#         return ( self.atzime1 + self.atzime)/2 
    
#     def show_info(self):
#         print(f"{ self.vards } vidējā atzīme ir { self.avarage_grade() }")



# Student1 = Student("Perrijs", 6, 7)

# Student1.show_info()

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# def calculate_average(atzimes):
#     return sum(atzimes / len(atzimes))

# class Student:
#     def __init__(self, vards, atzimes):
#         self.vards = vards
#         self.atzimes = atzimes

#     def max_grade(self):
#         return max(self.atzimes)
    
#     def is_excelent(self):
#         avg = calculate_average(self.grades)
#         if avg >= min_avg:
#             print(self.vards, "saņems Zelta piparkūku, jo vidējā atzīme ir ", avg)
#         else:
#             print(self.vards, "nesaņems Zelta piparkūku, jo vidējā atzīme ir ", avg)


# Student1 = Student("Perrijs", [6,7,9,10,10])


# -------------------------------------------------------------------------------------------------------------------------------------------------------

# from datetime import date

# class Transports:
#     def __init__(self, marka, maxAtrums, nobraukums, gads):
#         self.marka = marka
#         self.maxAtrums = maxAtrums
#         self.nobraukums = nobraukums
#         self.gads = gads
#         self.atrums = 0

#     def avarage_speed(self):
#         return date.today().year - int(self.gads)

# class Autobuss:
#     pass