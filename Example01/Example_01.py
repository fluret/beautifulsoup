import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
'''
Récupère toute la page HTML
'''

results = soup.find(id="ResultsContainer")
'''
Récupère le premier id égal à ResultsContainer, ici il n'y en a qu'un
'''
#print(results.prettify())

job_elements = results.find_all("div", class_="card-content")
'''
récupère sous la forme d'une liste toutes les divs possédant la classe card-content
'''
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    #Récupère la première balise h2 avec la classe title ici une seule
    company_element = job_element.find("h3", class_="company")
    #Récupère la première balise h3 avec la classe company ici une seule
    location_element = job_element.find("p", class_="location")
    # récupère la première balise p avec la classe location ici une seule
    print(title_element.text.strip())
    #imprime uniquement le texte de title_element et donc supprime les balises
    #la fonction strip supprime les esapces en début et en fin de chaine
    print(company_element.text.strip())
    
    print(location_element.text.strip())
    
    print()

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

print(len(python_jobs))
