from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from ..models import Product
from ..service.selenium_service import Browser
from typing import List
import time

class Sasoi006():

    def __init__(self, browser: Browser):
        self.__browser = browser
        self.__product_counter: int = int(0) 
        self.__product_limit: int = int(5)
    
    def get_browser(self):
        return self.__browser
    
    def set_product_counter(self, new_counter: int):
        self.__product_counter = new_counter
    
    def get_product_counter(self):
        return self.__product_counter
    
    def get_product_limit(self):
        return self.__product_limit
    
    def login(self, login: str, password: str, branch: str):
        self.get_browser()\
            .redirect_to("https://srvapp619.br-atacadao.corp/auth/login.do?lang=pt")
        
        # Username
        self.get_browser()\
            .wait_for_element(None, By.ID, 'j_username_fake', 4)\
            .send_keys(login)
        # Password
        self.get_browser()\
            .wait_for_element(None, By.ID, 'j_password_fake', 4)\
            .send_keys(password)
        # Login
        self.get_browser()\
            .wait_for_element(None, By.ID, 'entrar', 4)\
            .click()

        # Aguarda o tempo da pagina carregar
        time.sleep(1)

        # # Verifica se o usuário errou a senha, quando o usuário erra a senha o site mostra uma div com erro
        # error_div = WebDriverWait(self.get_browser().get_driver(), 1).until(
        #     EC.visibility_of_any_elements_located((By.CLASS_NAME, "error-message"))
        # )

        # if len(error_div) > 0:
        #     return False
        
        # Escolhe a filial que vamos logar... ¬¬
        branch_checkbox = self.get_browser()\
            .wait_for_element(None, By.ID, 'filialAutocomplete', 4)
        branch_checkbox.send_keys(branch)
        branch_checkbox.send_keys(Keys.ARROW_DOWN)
        branch_checkbox.send_keys(Keys.ENTER)

        # Confirma a entrada
        self.get_browser().wait_for_element(None, By.ID, 'entrarFilial', 4)\
            .click()
        
        # Redireciona para a tela SASOI006 do Save Web
        self.get_browser()\
            .redirect_to(f'https://srvapp{branch}.br-atacadao.corp/sasoi006/execute.do')
        
        return True
    
    # Esse método prepara a tela para enviar os códigos do SaveWeb para o TagSell
    def setup_tag(self):
        self.get_browser().wait_for_element(None, By.ID, 'tpImpressao_1', 4)\
            .click()
        
        # Clica no checkbox referente a 'Cartaz' no SaveWeb
        select_tag = self.get_browser()\
            .wait_for_element(None, By.ID, 'comboCartaz', 4)
        
        # Seleciona a opção A5 para enviar ao Tagsell
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ARROW_DOWN)
        select_tag.send_keys(Keys.ENTER)

    def fill_products(self, products: List[Product]):
        sended_products = []
        # Seleciona o campo para preencher o código do produto
        code_field = self.get_browser()\
            .wait_for_element(None, By.ID, 'codigoBarra', 4)
        
        self.setup_tag()

        # Percorre a lista de produtos e para cada produto preenche o campo de código
        for product in products:
            
            # Temos que adiconar 100 ao final do código para o sistema reconhecer o código completo
            code_field.send_keys(str(product.get_code())+'100') 
            code_field.send_keys(Keys.ENTER)
            self.set_product_counter(self.get_product_counter() + 1)
            sended_products.append(product.get_code())
            
            # Se os produtos preenchidos chegarem ao limite vamos tentar enviar para o TagSell
            if self.get_product_counter() == self.get_product_limit():
                self.send_to_tagsell()

        # Se não atigir o limite de produtos e ainda restar, vamos tentar enviar para o TagSell
        if self.get_product_counter() > 0:
            self.__send_to_tagsell()

        try:
            return sended_products
        finally:
            self.get_browser().get_driver().quit()
        

    def send_to_tagsell(self):
        self.get_browser()\
            .wait_for_element(None, By.ID, 'btnImprimir', 4)\
            .click()
        # Após enviar para o TagSell o sistema trava por uns 2 segundos, então tesmo que esperar
        time.sleep(2)
            
        # Após enviar para o TagSell temos que configurar novamente o checkbox para o modo Cartaz/A5  
        if self.get_product_counter() > 0:
            self.setup_tag()

        # Redefine a contagem de produtos
        self.set_product_counter(int(0))