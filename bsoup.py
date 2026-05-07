import requests
from bs4 import BeautifulSoup

# url = 'https://oxylabs.io/blog'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'lxml')

# paragraphs = soup.find_all("p")

# for p in paragraphs:
#     print(p.text)

#----------------------------------------------------------------------------------------

# texts = soup.find_all("span", class_="text")
# for c in texts:
#     print(c.text)

# 1.----------------------------------------------------------------------------------------


# url = 'https://t2v.lv/'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'lxml')

# print(soup.title)

# 2.----------------------------------------------------------------------------------------

# header = soup.find_all('h2')

# for h in header:
#     print(h.text)

# 3.----------------------------------------------------------------------------------------

# url = 'http://quotes.toscrape.com'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'lxml')

# name = soup.find_all(class_="author")

# for a in name:
#     print(a.text)

# 4.----------------------------------------------------------------------------------------


# quotes = soup.find_all(class_="text")

# for q in quotes:
#     print(q.text)

# with open ("citati_fails.txt","w") as fails:
#     for q in quotes:
#         fails.write(q.text)
#     print("Izveidots un aizpildīts jauns fails")

# 5.----------------------------------------------------------------------------------------

# quotes = soup.find_all(class_="text")

# b = 0

# for q in quotes:
#     b += 1

# print(f"lapā ir {b} citāti.")

# print(len(quotes))
