from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.model.product import Product
from src.model.browser import Browser
from typing import List
import time

class Sasoi006():

    __products: List[Product] = []
    __browser: Browser = None
    __product_counter: int = int(0)
    __product_limit: int = int(21)

    def __init__(self, browser: Browser, products: List[Product]):
        self.__products = products
        self.__browser - browser

    def get_products(self):
        return self.__products
    
    def get_browser(self):
        return self.__browser
    
    def set_product_counter(self, new_counter: int):
        self.__product_counter = new_counter
    
    def get_product_counter(self):
        return self.__product_counter
    
    def get_product_limit(self):
        return self.__product_limit
    
    def sasoi006_login(self, login: str, password: str, branch: str):
        # Username
        self.get_browser()\
            .wait_for_be_clickable(By.ID, 'j_username_fake')\
            .send_keys(login)
        # Password
        self.get_browser()\
            .wait_for_be_clickable(By.ID, 'j_username_fake')\
            .send_keys(password)
        # Login
        self.get_browser()\
            .wait_for_element(By.ID, 'entrar')\
            .click()
        
        # Escolhe a filial que vamos logar... ¬¬
        branch_checkbox = self.get_browser()\
            .wait_for_element(By.ID, 'filialAutocomplete')
        branch_checkbox.send_keys(branch)
        branch_checkbox.send_keys(Keys.ARROW_DOWN)
        branch_checkbox.send_keys(Keys.ENTER)

        # Confirma a entrada
        self.get_browser().wait_for_element(By.ID, 'entrarFilial')\
            .click()
        
        # Redireciona para a tela SASOI006 do Save Web
        self.get_browser().__redirect_to(f'https://srvapp{branch}.br-atacadao.corp/sasoi006/execute.do')
    
    # Esse método prepara a tela para enviar os códigos do SaveWeb para o TagSell
    def setup_tag(self, type: str):
        self.get_browser().wait_for_element(By.ID, 'tpImpressao_1')\
            .click()
        
        # Clica no checkbox referente a 'Cartaz' no SaveWeb
        select_tag = self.get_browser()\
            .wait_for_element(By.ID, 'comboCartaz')
        
        # Seleciona a opção A5 para enviar ao Tagsell
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ENTER)

    def fill_products(self):
        # Seleciona o campo para preencher o código do produto
        code_field = self.get_browser()\
            .wait_for_element(By.ID, 'codigoBarra')
        
        # Percorre a lista de produtos e para cada produto preenche o campo de código
        for product in self.get_products():

            # Temos que adiconar 100 ao final do código para o sistema reconhecer o código completo
            code_field.send_keys(product.get_code()+'100') 
            code_field.send_keys(Keys.ENTER)
            self.set_product_counter(self.get_product_counter() + 1)
            
            # Se os produtos preenchidos chegarem ao limite vamos tentar enviar para o TagSell
            if self.get_product_counter() == self.get_product_limit():
                self.send_to_tagsell()

            # Se não atigir o limite de produtos e ainda restar, vamos tentar enviar para o TagSell
            if self.get_product_counter() > 0:
                self.send_to_tagsell()

    def send_to_tagsell(self):
        self.get_browser()\
            .wait_for_element(By.ID, 'btnImprimir')\
            .click()
        # Após enviar para o TagSell o sistema trava por uns 2 segundos, então tesmo que esperar
        time.sleep(2)
            
        # Após enviar para o TagSell temos que configurar novamente o checkbox para o modo Cartaz/A5  
        if self.get_product_counter() > 0:
            self.setup_tag()

        # Redefine a contagem de produtos
        self.set_product_counter(int(0))