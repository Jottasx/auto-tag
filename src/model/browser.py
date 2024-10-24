from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.remote.webelement import WebElement


class Browser():

    def __init__(self, path: str) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service(path)
        self.__driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_driver(self):
        return self.__driver

    def __redirect_to(self, url: str):
        self.__driver.get(url)

    def wait_for_element(self, by: By, identification: str):
        return WebDriverWait(self.__driver, 4).until(
            EC.visibility_of_element_located((by, identification))
        )
    
    def wait_for_be_clickable(self, by: By, identification: str):
        return WebDriverWait(self.__driver, 4).until(
            EC.element_to_be_clickable((by, identification))
        )
    
    def login(self, login: str, password: str):
        self.__redirect_to("https://app.tagsell.com.br/login")
        self.__wait_for_element(self.__driver, By.ID, 'email').send_keys(login)
        self.__wait_for_element(self.__driver, By.ID, 'password').send_keys(password)
        self.__wait_for_element(self.__driver, By.XPATH, '//button[@type="submit"]').click()

    def open_new_tab(self, el: WebElement):
        ActionChains(self.__driver).key_down(Keys.CONTROL).click(el).key_up(Keys.CONTROL).perform()


    
