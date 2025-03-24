class Map:
    def __init__(self):
        self.ifs_acronimo = ["IFAC" ]
        
        self.ifs_extenso = [
       "Instituto Federal de Educação, Ciência e Tecnologia do Acre"
         ]
        
        self.ifs_extenso_lim = ["Instituto Federal do Acre"
        ]
        
        self.ifs_federacao = ["Acre"
        ]
    def map_ifs_acronimo(self):        
        return self.ifs_acronimo
    
    def map_ifs_extenso(self):
        return self.ifs_extenso

    def map_ifs_extenso_lim(self):
        return self.ifs_extenso_lim
        
    def map_ifs_federacao(self):        
        return self.ifs_federacao
    
    def map_interval(self, year):
        
        year_verificted = self.verificar(year)
        if year_verificted==False:
            interval = {
                "janeiro":{
                    "init": f"01/01/{year}",
                    "end": f"31/01/{year}"
                },
                "fevereiro":{
                    "init": f"01/02/{year}",
                    "end": f"28/02/{year}"
                },
                "marco":{
                    "init": f"01/03/{year}",
                    "end": f"31/03/{year}"
                },
                "abril":{
                    "init": f"01/04/{year}",
                    "end": f"30/04/{year}"
                },
                "maio":{
                    "init": f"01/05/{year}",
                    "end": f"31/05/{year}"
                },
                "junho":{
                    "init": f"01/06/{year}",
                    "end": f"30/06/{year}"
                },
                "julho":{
                    "init": f"01/07/{year}",
                    "end": f"31/07/{year}"
                },
                "agosto":{
                    "init": f"01/08/{year}",
                    "end": f"31/08/{year}"
                },
                "setembro":{
                    "init": f"01/09/{year}",
                    "end": f"30/09/{year}"
                },
                "outubro":{
                    "init": f"01/10/{year}",
                    "end": f"31/10/{year}"
                },
                "novembro":{
                    "init": f"01/11/{year}",
                    "end": f"30/11/{year}"
                },
                "dezembro":{
                    "init": f"01/12/{year}",
                    "end": f"31/12/{year}"
                }
            }
            
            return interval
        else:
            interval = {
               "janeiro":{
                    "init": f"01/01/{year}",
                    "end": f"31/01/{year}"
                },
                "fevereiro":{
                    "init": f"01/02/{year}",
                    "end": f"29/02/{year}"
                },
                "marco":{
                    "init": f"01/03/{year}",
                    "end": f"31/03/{year}"
                },
                "abril":{
                    "init": f"01/04/{year}",
                    "end": f"30/04/{year}"
                },
                "maio":{
                    "init": f"01/05/{year}",
                    "end": f"31/05/{year}"
                },
                "junho":{
                    "init": f"01/06/{year}",
                    "end": f"30/06/{year}"
                },
                "julho":{
                    "init": f"01/07/{year}",
                    "end": f"31/07/{year}"
                },
                "agosto":{
                    "init": f"01/08/{year}",
                    "end": f"31/08/{year}"
                },
                "setembro":{
                    "init": f"01/09/{year}",
                    "end": f"30/09/{year}"
                },
                "outubro":{
                    "init": f"01/10/{year}",
                    "end": f"31/10/{year}"
                },
                "novembro":{
                    "init": f"01/11/{year}",
                    "end": f"30/11/{year}"
                },
                "dezembro":{
                    "init": f"01/12/{year}",
                    "end": f"31/12/{year}"
                }
            }
            return interval
    def verificar(self, ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
       
        
#if baiano, if sertao pe, ifg, ifpb, 
            
            

