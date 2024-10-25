from src.model.browser import Browser
from selenium.webdriver.remote.webelement import WebElement
import time


class TagSell():

    def __init__(self, browser: Browser):
        self.__browser = browser

    def __get_browser(self):
        return self.__browser
    
    def scroll_table(self, table: WebElement):
        last_height = self.__get_browser()\
            .get_driver()\
            .execute_script("return arguments[0].scrollHeight", table)
    
        while True:
            # Fazer scroll até o final da tabela
            self.__get_browser()\
                .get_driver()\
                .execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", table)
            time.sleep(2)  # Aguarda o carregamento de novos elementos
            
            # Verifica se novos elementos foram carregados
            new_height = self.__get_browser()\
                .get_driver()\
                .execute_script("return arguments[0].scrollHeight", table)
            
            if new_height == last_height:
                break  # Se não houver mais conteúdo para carregar, para o scroll

            last_height = new_height