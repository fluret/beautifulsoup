import re

from bs4 import BeautifulSoup
import requests

# envoyer une requête http pour récupérer le contenu HTML
url = "https://www.sanfoundry.com/python-mcqs-lists-1/"
response = requests.get(url)
html_content = response.content

# utiliser BeautifulSoup pour parser le contenu HTML
soup = BeautifulSoup(html_content, "html.parser")

# récupérer le contenu de la balise div possédant la classe "entry-content"
entry_content = soup.find("div", class_="entry-content")

# Initialize an empty list to store the contents of the selected p tags
contenu = []

for p in entry_content.find_all("p"):
    match = re.match(r"^\d{1,2}\.", p.get_text())
    if match:
        contenu.append(p)

print(contenu)
# for val in contenu:
#     print(val.split("<br>"))