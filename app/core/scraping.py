from app.models.Publication import Publication
import time
from bs4 import BeautifulSoup
import requests
import re

year = 2018
class Scraping:
    def __init__(self,collecion, month, year, urls):
        self.collecion = collecion
        self.month = month
        self.year = year
        self.urls = urls
        
    def scraping(self):
        print("Iniciando extracao...")
        pub = []
        for url in self.urls:
            html = requests.get(url, verify=False)
            beautifulSoup = BeautifulSoup(html.content, 'html.parser')
            
            date = beautifulSoup.find('span', class_='publicado-dou-data')
            if date:
                date = date.get_text()
            else:
                date = "Sem data"
            organ = beautifulSoup.find('span', class_='orgao-dou-data')
            if organ:
                organ = organ.get_text()
            else:
                organ = "Sem órgão"
            concierge = beautifulSoup.find('p', class_='identifica')
            if concierge:
                concierge = concierge.get_text()
            else:
                concierge = beautifulSoup.find('h3', class_='titulo-dou')
                concierge = concierge.find('span').get_text()
            
            content = beautifulSoup.find('div', class_='texto-dou')
            if content:
                extract = content.find('p', class_='identifica')
                if extract:
                    extract.extract()
                elif content.find('h3', class_='titulo-dou'):
                    extract = content.find('h3', class_='titulo-dou')
                    extract.extract()
                content = content.get_text()
            else:
                content = "Sem conteúdo"
            responsible = beautifulSoup.find('p', class_='assina')
            if responsible:
                responsible = responsible.get_text()
            type = self.get_type(content=content)
            publication = Publication(self.collecion, type, organ,content, concierge ,date ,responsible, self.month, self.year, url)
            pub.append(publication)
        return pub
           
        
       
                
    def get_type(self, content):
        nomecao = re.compile(r'\b(NOMEAR|Nomear|nomear|NOMEIA|Nomeia|nomeia)\b')
        exoneracao = re.compile(r'\b(EXONERAR|Exonerar|exonerar|EXONERA|Exonera|exonera)\b')
        
        #verificação
        if nomecao.search(content):
            return "Nomeação"
        elif exoneracao.search(content):
            return "Exoneração"
        else:
            return "Outro"
        
    
   