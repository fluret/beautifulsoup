import re
from bs4 import BeautifulSoup
import requests

# envoyer une requête http pour récupérer le contenu HTML
url = "https://www.sanfoundry.com/python-mcqs-lists-1/"
response = requests.get(url)
html_content = response.content

# utiliser BeautifulSoup pour parser le contenu HTML
soup = BeautifulSoup(html_content, "html.parser")

# Initialize an empty list to store the contents of the selected p tags
contenu = []
for p in soup.find_all("p"):
    match = re.match(r"^\d{1,2}\.", p.get_text())
    if match:
        for element in p.contents:
            if element.name == 'br':
                contenu.append(element.previous_sibling.strip())
            # if element.name is None:
            #     contenu.append(element.strip())

print(contenu)