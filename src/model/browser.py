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

import time
import re


class Browser():

    driver: webdriver.Chrome = None

    def __init__(self, path: str) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service(path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def __redirect_to(self, url: str):
        self.driver.get(url)

    def __wait_for_element(self, by: By, identification: str):
        return WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((by, identification))
        )
    
    def login(self, login: str, password: str):
        self.__redirect_to("https://app.tagsell.com.br/login")
        self.__wait_for_element(self.driver, By.ID, 'email').send_keys(login)
        self.__wait_for_element(self.driver, By.ID, 'password').send_keys(password)
        self.__wait_for_element(self.driver, By.XPATH, '//button[@type="submit"]').click()

    def open_new_tab(self, el: WebElement):
        ActionChains(self.driver).key_down(Keys.CONTROL).click(el).key_up(Keys.CONTROL).perform()


    
