import re
from bs4 import BeautifulSoup
import requests
import copy

# envoyer une requête http pour récupérer le contenu HTML
url = "https://www.sanfoundry.com/python-mcqs-lists-1/"
response = requests.get(url)
html_content = response.content

# utiliser BeautifulSoup pour parser le contenu HTML
soup = BeautifulSoup(html_content, "html.parser")

# Initialize an empty list to store the contents of the selected p tags
contenu = []
for p in reversed(soup.find_all("p")):
    for data in p.select("p"):
        data.decompose()
    for data in p.find_all("div" , class_="sf-mobile-ads"):
        data.decompose()
    for data in p.find_all("span"):
        data.decompose()
    match = re.match(r"^\d{1,2}\.", p.get_text())        
    if match:
        for element in p.contents:
            if element.name == 'br':
                contenu.append(element.previous_sibling.strip())
    b = p.find("div" , class_="collapseomatic_content")
    if b:
        contenu.append(b.text)
    p.decompose()
print(contenu)