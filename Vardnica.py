# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }



# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change

# # ------------------------------------------------------------

# x = car.values()
# print(x) #before the change
# car["color"] = "red"
# print(x) #after the change

# # ------------------------------------------------------------

# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

# # ------------------------------------------------------------

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# # ------------------------------------------------------------

#   thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

# 1.uzd ------------------------------------------------------------

# skoleni = {
#     "Anna" : 9,  
#     "Liene" : 10,
#     "Māris" : 8,  
#     "Beāte" : 6,
#     "Rihards" :7

# }

# x = skoleni.keys()
# print(x)
# y = skoleni.values()
# print(y)

# print(skoleni["Anna"])

# skoleni["Pēteris"] = 3

# print(skoleni)

# skoleni.pop("Māris")

# print(skoleni)

# if "Mārtiņš" in skoleni:
#   print("Yes, 'Mārtiņš' is one of the keys in the thisdict dictionary")
# else:
#   print("No, 'Mārtiņš' is not one of the keys in the thisdict dictionary")

# 3.uzd ------------------------------------------------------------

cars = {
    "Ford" : 1951,  
    "Opel" : 1991,
    "Audi" : 2002,  
    "Tesla" : 2017,
    "BMW" :2005
}

for x,y in cars.items():
    print(x,y)

if "Audi" in cars:
  print("Yes, 'Audi' is one of the keys in the thisdict dictionary")
else:
  print("No, 'Audi' is not one of the keys in the thisdict dictionary")

for x,y in cars.items():
    if y > 2010:
       print(x)
    else:
       pass