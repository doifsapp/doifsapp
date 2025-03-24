from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
import re
import time

class Crawler:
    def __init__(self, if_, ifs_add, if_federacao, init, end):
        self.if_ = if_
        self.ifs_add = ifs_add
        self.if_uni = if_federacao
        self.init = init
        self.end = end
        chromedriver_path = r'Chromedriver\chromedriver.exe' 
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.url = 'https://www.in.gov.br/acesso-a-informacao/dados-abertos/base-de-dados'
        self.all_links = []
        self.m = []

    def crawler(self):
        try:
            self.driver.get(self.url)
            input_text = self.driver.find_element(By.CSS_SELECTOR, 'input#search-bar')
            input_text.send_keys(self.if_)

            button_advance = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a#toggle-search-advanced'))
            )
            button_advance.click()
            #tempo de espera
            time.sleep(5)
            result_exact = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#tipo-pesquisa-1'))
            )
            result_exact.click()
            #tempo de espera
            time.sleep(3)
            section_dou = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#do2'))
            )
            section_dou.click()
            #tempo de espera
            time.sleep(3)
            ediction = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#personalizado'))
            )
            ediction.click()
            #tempo de espera
            time.sleep(4)
            periodo_init = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, 'data-inicio'))
            )
            self.driver.execute_script(f"arguments[0].value = '{self.init}';", periodo_init)

            periodo_end = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'data-fim'))
            )
            self.driver.execute_script(f"arguments[0].value = '{self.end}';", periodo_end)
            #tempo de espera
            time.sleep(3)
            search = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button'))
            )
            search.click()

            WebDriverWait(self.driver, 15).until(EC.url_changes(self.url))

            links = self.result_urls()
            self.m.extend(links)
            links_add = []

            for k in self.ifs_add:
                input_text = self.driver.find_element(By.CSS_SELECTOR, 'input#search-bar')
                input_text.clear()
                input_text.send_keys(k)

                button_advance = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, 'a#toggle-search-advanced'))
                )
                button_advance.click()

                #tempo de espera
                time.sleep(4)
                search = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button'))
                )
                search.click()
                #tempo de espera
                time.sleep(4)
                urls = self.result_urls() #chamada da função
                links_add.extend(urls)
            self.driver.quit() #fechamento da navegador
            self.m.extend(links_add)
            print(f"Total de URLs (sem criterio) -> {len(self.m)}")
            pre_urls = self.m
            print("Retornando URLs..")
            urls_filter = self.filter_result(self.if_uni, pre_urls)
            print("Filtrando resultados...")
            print(f"URLS apenas da federacao -> {len(urls_filter)}")
            
            urls_clean = self.urls_filter_clean(urls_filter)
            print("Eliminando URLs repetidas...")
            print(f"URLS sem repeticao -> {len(urls_clean)}")
            self.all_links.extend(urls_clean)
            print("Finalizado com sucesso!!")
            
            return self.all_links
            
        except Exception as error:
            print("Erro exception", error)
        finally:
            self.driver.quit()

    def result_urls(self):
        urls_all = []
        while True:
            try:
                link_elements = self.driver.find_elements(By.CSS_SELECTOR, 'h5.title-marker a')
                links = [element.get_attribute('href') for element in link_elements]
                links = [link for link in links if link]

                urls_all.extend(links)
                next_button = self.driver.find_element(By.CSS_SELECTOR, 'button#rightArrow')
                is_disabled = next_button.get_attribute('disabled')
                if is_disabled:
                    break
                else:
                    ActionChains(self.driver).click(next_button).perform()
                    WebDriverWait(self.driver, 15).until(EC.staleness_of(next_button))
            except Exception as exception:
                print(f"Página sem resultados. ERRO: {exception}")
                break

        urls_all.reverse()
        return urls_all
    
    def filter_result(self, if_federacao, urls):
        urls_all = []
        for link in urls:
            try:
                html = requests.get(link, verify=False)
                html.raise_for_status()
                beautifulSoup = BeautifulSoup(html.content, 'html.parser')
                orgao = beautifulSoup.find("span", class_='orgao-dou-data')
                concierge = beautifulSoup.find('p', class_='identifica')
                if concierge:
                    concierge = concierge.get_text()
                else:
                    concierge = beautifulSoup.find('h3', class_='titulo-dou')
                    concierge = concierge.find('span').get_text()
                
                if orgao:
                    orgao_text = orgao.get_text()
                    if (re.search(r'\b' + re.escape(if_federacao) + r'\b', orgao_text) or
                        orgao_text == 'Reitoria' or orgao_text == 'Gabinete') and \
                    not re.search(r'\bRETIFICAÇÃO\b', concierge):  # Negação para "RETIFICAÇÂO"
                    
                        urls_all.append(link)

            except requests.RequestException as e:
                print(f"Erro ao fazer a requisição: {link}")
            except Exception as e:
                print(f"Erro ao processar o link: {link}")
                
        
        return urls_all


    def urls_filter_clean(self, urls):
        return list(dict.fromkeys(urls))
