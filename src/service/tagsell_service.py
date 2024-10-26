from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.model.product import Product
from src.model.browser import Browser
from typing import List
import time
import re


class TagSell():

    def __init__(self, browser: Browser):
        self.__browser = browser
        self.__product_rows = []

    def __get_browser(self):
        return self.__browser
    
    def get_product_rows(self):
        return self.__product_rows  
    
    # Médoto para fazer login no TagSell
    def login(self, login: str, password: str):
        self.__get_browser()\
            .redirect_to("https://app.tagsell.com.br/login")
        self.__get_browser()\
            .wait_for_element(el=None, by=By.ID, identification='email')\
            .send_keys(login)
        self.__get_browser()\
            .wait_for_element(el=None, by=By.ID, identification='password')\
            .send_keys(password)
        self.__get_browser()\
            .wait_for_element(el=None, by=By.XPATH, identification='//button[@type="submit"]')\
            .click()
        
        time.sleep(1)

        # Se a página já estiver nos cartazes, não vai precisar redirecionar
        link = "https://app.tagsell.com.br/online/posters"
        driver = self.__get_browser().get_driver()
        if driver.current_url != link:
            self.__get_browser().redirect_to("https://app.tagsell.com.br/online/posters")

        time.sleep(1)

    # Médoto para rolar a tabela dinânica para que todos os elementos fiquem visíveis
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

    # Médoto para preencher a lista de linhas HTML dos produtos
    def set_product_rows(self, products: List[Product]):
        # Preenche uma lista somente com os códigos internos dos produtos
        product_codes = []
        for product in products:
            product_codes.append(product.get_code())

        # Tabela HTML do TagSell
        table = self.__get_browser()\
            .wait_for_element(None, By.CSS_SELECTOR, ".table.table-striped.table-fw-widget.table-hover")
        
        # Rola a tabela até o fim
        self.scroll_table(table)
        
        # Linhas da tabela
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Para cada linha na lista de linhas
        for row in rows:
            for product in products:
                if self.__is_in_row(product.get_code(), row):
                    self.__product_rows.append(row)
            

    # Método para verificar se um código de um produto está em uma linha HTML
    def __is_in_row(self, code: str, row: WebElement) -> bool:
        rows = self.get_product_rows()
        
        td_list = row.find_elements(By.TAG_NAME, "td")
        # Para cada <td> dentro da linha
        for td in td_list:
            match = re.search(r':p:(\d+):d', td.text) # 5 digitos númericos entre :p: e :d
            # Verifica se algum <td> possui o código interno do produto
            if match:
                code_found = match.group(1) # Salva o código encontrado
                if int(code_found) == code:
                    return True
        return False

                    
    # Médoto para editar um único produto
    def edit_product(self, product: Product) -> Product:
        driver = self.__get_browser().get_driver()
        # Percorre as janelas abertas do Browser
        for window_handle in driver.window_handles:
            driver.switch_to.window(window_handle)

            # Verifica se a janela atual aberta é a do link do produto
            if driver.current_url == product.get_link():
                time.sleep(1) # Aguarda a aba ser escolhida

                # Selecionando os inputs de embalagem, preço e o botão de salvar
                input_emb = self.__get_browser()\
                    .wait_for_element(
                        By.XPATH,
                        "//label[contains(text(),'Embalagem de atacado')]/following-sibling::input"
                    )
                input_price = self.__get_browser()\
                    .wait_for_element(
                        By.XPATH,
                        "//label[contains(text(),'Preço no Varejo')]/following-sibling::input"
                    )
                btn_save = self.__get_browser()\
                    .wait_for_element(
                        By.XPATH,
                        "//div[contains(@class, 'div-btns')]//a"
                    )

                # Aqui queremos somente quantidade dentro da caixa : 
                # CXA 1 X 36 X 142G -> 36
                emb_box_number = product.get_emb().split(" X ")[1]

                # Aqui temos que copiar o conteúdo do input da embalagem para usarmos depois
                input_emb_value = input_emb.get_attribute("value")
                input_emb.clear()

                # Agora vamos atualizar o input da embalagem com o novo valor caso tenha
                if input_emb_value != '':
                    # Resultado esperado -> CXA C/ XX R$ XX,XX
                    input_emb.send_keys(
                        f"{input_emb_value.split('R$ ')[0]}R$ {(product.get_price() * emb_box_number):.2f}".replace(".", ",")
                    )

                # Atualiza o preço do produto
                input_price.clear()
                input_price.send_keys(product.get_price())

                # Salva as alterações do produto no TagSell
                btn_save.click()

                time.sleep(1)

                product.set_edited(True)
                return product


    # Médoto para abrir um produto em outra aba
    def open_product_in_new_tab(self, product_row: WebElement, product: Product):
        # Seleciona o Edit_Button e preenche o link do produto
        edit_button = self.__get_browser()\
            .wait_for_element(element=product_row, by=By.XPATH, identification='.//a[@title="Editar"]')
        
        # Preenche o ID e o Link do produto
        product.set_id(edit_button.get_attribute("href").split("/")[-2])
        product.set_product_link(edit_button.get_attribute("href"))

        self.__get_browser()\
            .get_driver()\
            .execute_script(f"window.open('{product.get_link()}', '_blank');")
    
    # Médoto para fechar as abas dos produtos que já foram editados
    def close_printed_products_tabs(self, products: List[Product]):
        driver = self.__get_browser().get_driver()
        main_window: str|None = None
        # Percorre a lista de abas abertas e procura a página principal
        for window in driver.window_handles:
            driver.switch_to.window(window)
            if driver.current_url == "https://app.tagsell.com.br/online/posters":
                main_window = window
        
        for product in products:
            # Para cada aba aberta no navegador verifica se o link do produto bate, se ele já foi editado e fecha a aba.
            for window in driver.window_handles:
                driver.switch_to.window(window)
                if driver.current_url == product.get_link() and product.is_edited == True:
                    driver.close()

        # Voltar para a aba principal
        driver.switch_to.window(main_window)


    # Médoto para imprimir um produto
    def print_products(self, products: List[Product]):
        rows = self.get_product_rows()
        for row in rows:
            row_id = self.__get_browser()\
                    .wait_for_element(el=row, by=By.XPATH, identification='.//a[@title="Editar"]')\
                    .get_attribute("href")\
                    .split("/")[-2]
            
            for product in products:
                # Verifica se o ID é o mesmo do produto e seleciona o checkbox para impressão
                if row_id == product.get_id() and product.is_edited() == True:
                    row.find_element(By.TAG_NAME, "td")\
                        .find_element(By.ID, f"selectable-{product.get_id()}")\
                        .click()
                    time.sleep(1)
                    product.set_printed(True)
                
            # O botão de imprimir só aparece após 1 ou mais checkbox forem selecionados
            self.__get_browser()\
                .wait_for_element(None, By.ID, 'printButton')\
                .click()
            
            time.sleep(1)
            
            # Clica no botão sim do modal
            self.__get_browser()\
                .wait_for_element(None, By.XPATH, "//h5[contains(text(), 'Tem certeza que deseja imprimir?')]/ancestor::div[contains(@class, 'modal-content')]//button[contains(text(), 'Sim')]")\
                .click()
            
            time.sleep(1)

            # Navegar para a aba que acabou de abrir com as impressões
            driver = self.__get_browser().get_driver()
            tabs = driver.window_handles
            original_window = tabs[0]
            # A impressão é automaticamente feita em PDF e salvo em Downloads devido as configurações do Driver
            driver.switch_to.window(tabs[-1])

            time.sleep(1)

            driver.close()
            # Retorna para a aba principal
            driver.switch_to.window(original_window)
            time.sleep(0.5)
