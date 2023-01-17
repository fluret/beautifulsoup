from bs4 import BeautifulSoup, NavigableString
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
contenu = ""

for element in entry_content.contents:
    if isinstance(element, NavigableString):
        contenu += element
    elif element.name == 'span' and 'collapseomatic' in element['class']:
        break
    else:
        contenu += element.get_text()

print(contenu)