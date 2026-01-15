# 1. uzd ----------------------------------------------------------------------------------------------------------

# class Darbinieks:
#     def __init__(self, vards, amats):
#         self.vards = vards
#         self.amats = amats


# jauns_darbinieks = Darbinieks("Anna","Projekta vadītāja")

# print(jauns_darbinieks.vards)
# print(jauns_darbinieks.amats)

# 2. uzd ----------------------------------------------------------------------------------------------------------

# class Darbinieks:
#     def __init__(self, vards, amats):
#         self.vards = vards
#         self.amats = amats
#     def radit_profilu(self):
#         print("Darbinieks: " + self.vards + ", Amats: " + self.amats)


# jauns_darbinieks = Darbinieks("Anna","Projekta vadītāja")

# jauns_darbinieks.radit_profilu()

# 3. uzd ----------------------------------------------------------------------------------------------------------

# from tkinter import messagebox
# class Darbinieks:
#     def __init__(self, vards, amats, alga = 3000):
#         self.vards = vards
#         self.amats = amats
#         self.alga = alga

#     def paaugstinat_algu(self, summa):
#         self.alga += summa
#         messagebox.showinfo("Paaugstinājums!", f"Jaunā alga ir: {self.alga}")      

#     def radit_profilu(self):
#         print("Darbinieks: " + self.vards + ", Amats: " + self.amats + ", Alga:" , self.alga)




# jauns_darbinieks = Darbinieks("Anna","Projekta vadītāja")



# jauns_darbinieks.paaugstinat_algu(500)

# jauns_darbinieks.radit_profilu()

# 4.uzd ------------------------------------------------------------------------------------------------------------------

# from tkinter import messagebox
# class Darbinieks:
#     def __init__(self, vards, amats, alga = 2000):
#         self.vards = vards
#         self.amats = amats
#         self.alga = alga

#     def paaugstinat_algu(self, summa):
#         self.alga += summa
#         messagebox.showinfo("Paaugstinājums!", f"Jaunā alga ir: {self.alga}")      
         
#     def radit_profilu(self):
#         print("Darbinieks: " + self.vards + ", Amats: " + self.amats + ", Alga:" , self.alga)




# jauns_darbinieks = Darbinieks("Anna","Projekta vadītāja")

# vecs_darbinieks = Darbinieks("Jānis","Analītiķis")



# jauns_darbinieks.paaugstinat_algu(500)

# jauns_darbinieks.radit_profilu()

# vecs_darbinieks.radit_profilu()

# 5.uzd ------------------------------------------------------------------------------------------------------------------

# from tkinter import messagebox
# class Darbinieks:
#     def __init__(self, vards, amats, alga = 2000):
#         self.vards = vards
#         self.amats = amats
#         self.alga = alga

#     def paaugstinat_algu(self, summa):

#         if summa > 0:
#             self.alga += summa
#             messagebox.showinfo("Paaugstinājums!", f"Jaunā alga ir: {self.alga}")    
#         else:
#             messagebox.showwarning("Kļūda!","Algas paaugstinājums nevar būt negatīvs vai nulle")

         
#     def radit_profilu(self):
#         print("Darbinieks: " + self.vards + ", Amats: " + self.amats + ", Alga:" , self.alga)




# jauns_darbinieks = Darbinieks("Anna","Projekta vadītāja")

# vecs_darbinieks = Darbinieks("Jānis","Analītiķis")



# jauns_darbinieks.paaugstinat_algu(200)

# jauns_darbinieks.paaugstinat_algu(-100)