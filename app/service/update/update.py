from app.models.Map import Map
from app.core.crawler import Crawler
from app.core.scraping import Scraping
from app.service.database.publicationDAO import PublicationDAO
from app.models.Publication import Publication
import time
from itertools import zip_longest


class UpdateDatabase:
    def __init__(self, year):
        self.year = year
        self.ifs_acr = Map().map_ifs_acronimo()
        self.ifs_extenso = Map().map_ifs_extenso()  # Armazena a primeira lista
        self.ifs_extenso_lim = Map().map_ifs_extenso_lim()  # Armazena a segunda lista
        self.if_fereacao = Map().map_ifs_federacao()
        self.interval = Map().map_interval(self.year)
       
        
    def update(self):
        print("Iniciando atualização...")
        
          # Instanciação fora do loop
        
        try:
            for month, interv in self.interval.items():
                publicationDAO = PublicationDAO()
                for n, (ifs_acr, if_ext, if_ext_lim, if_federacao) in enumerate(zip_longest(self.ifs_acr, self.ifs_extenso, self.ifs_extenso_lim, self.if_fereacao)):
                    ifs_add = [if_ext, if_ext_lim]  # Cria a lista com os dois elementos desejados

                    indexs = Crawler(ifs_acr, ifs_add, if_federacao, interv["init"], interv["end"]).crawler()
                    publications = Scraping(ifs_acr, month, self.year, indexs).scraping()
                    
                    print("Fim da extração")
                    print(ifs_acr, ifs_add, month, if_federacao )
                    print("Armazenando no database...")
                    
                    for publication in publications:
                        publicationDAO.create(publication)
                    print("Armazenamento concluido!")
                publicationDAO.close()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
        finally:
            publicationDAO.close()  # Garantia de fechamento da conexão