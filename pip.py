import requests
# response = requests.get("https://t2v.lv")
# print(response.status_code)

# response = requests.get("https://api64.ipify.org?format=text")

# print(f"Tava publiskā IP adrese: {response.text}")

# response = requests.get("https://catfact.ninja/fact")

# data = response.json()
# print(f"Nejaušs fakts par kaķiem: {data['fact']}")


# response = requests.get("https://api.chucknorris.io/jokes/random")

# data = response.json()
# print(data['value'])

#------------------------------------------------------------------------------------------

# response = requests.get("https://v2.jokeapi.dev/joke/Programming?format=txt")
# print(response.text)

# response = requests.get("https://v2.jokeapi.dev/joke/Pun")

# data = response.json()
# print(data['category'])
# print(data['type'])



# for i in range(3):

#     response = requests.get("https://v2.jokeapi.dev/joke/Pun")

#     data = response.json()

#     if data['type'] == 'single':
#         print (data['joke'])
#     else:
#         print(data['setup'])
#         print(data['delivery'])

# kategorija = input("Izvēlies joka kategoriju! (Programming/Misc/Dark/Pun/Spooky/Christmas): ")

# response = requests.get(f"https://v2.jokeapi.dev/joke/{kategorija}")

# data = response.json()

# if data['type'] == 'single':
#     print (data['joke'])
# else:
#     print(data['setup'])
#     print(data['delivery'])