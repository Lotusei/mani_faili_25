import requests
response = requests.get("https://t2v.lv")
print(response.status_code)

response = requests.get("https://api64.ipify.org?format=text")

print(f"Tava publiskā IP adrese: {response.text}")

# response = requests.get("https://catfact.ninja/fact")

# data = response.json()
# print(f"Nejaušs fakts par kaķiem: {data['fact']}")


response = requests.get("https://api.chucknorris.io/jokes/random")

data = response.json()
print(data['value'])

response = requests.get("https://api.chucknorris.io/jokes/random?category='dev'")

data = response.json()
print(data['value'])