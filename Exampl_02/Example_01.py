from bs4 import BeautifulSoup
import requests

# envoyer une requête http pour récupérer le contenu HTML
url = "https://www.sanfoundry.com/python-mcqs-lists-1/"
response = requests.get(url)
html_content = response.content

# utiliser BeautifulSoup pour parser le contenu HTML
soup = BeautifulSoup(html_content, "html.parser")

# récupérer le texte de la balise h1 possédant la classe "entry-title"
categorie = soup.find("h1", class_="entry-title").text

contenu = soup.find("div", class_="entry-content").contents

