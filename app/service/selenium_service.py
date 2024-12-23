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
        chrome_options.add_argument('--kiosk-printing')
        chrome_options.add_experimental_option("prefs", {
            "printing.print_preview_sticky_settings.appState": '{"recentDestinations":[{"id":"Save as PDF","origin":"local"}],"selectedDestinationId":"Save as PDF","version":2}',
            "savefile.default_directory": "C:\\Users\\lovej\\Downloads\\"
        })
        service = Service(path)
        self.__driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_driver(self):
        return self.__driver

    def redirect_to(self, url: str):
        self.__driver.get(url)

    def wait_for_element(self, el: WebElement|None, by: By, identification: str, timeout: float):
        # Se for recebido um elemento HTML, ele será usado
        #  caso contrário por padrão será usado o driver do Browser
        target = (self.__driver if el == None else el)
        return WebDriverWait(target, timeout).until(
            EC.visibility_of_element_located((by, identification))
        )
    
    
    def open_new_tab(self, el: WebElement):
        ActionChains(self.__driver).key_down(Keys.CONTROL).click(el).key_up(Keys.CONTROL).perform()


    
