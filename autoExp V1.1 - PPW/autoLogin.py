from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import reOpen

class Browser:
    browser, service=None, None
    def __init__(self, driver:str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service = self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by,value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def elok(self, username: str,password: str):
        self.click_button(by=By.LINK_TEXT, value='SSO UGM')
        self.add_input(by=By.ID, value='username', text=username)
        self.add_input(by=By.ID, value='password', text=password)
        self.click_button(by=By.NAME, value='submit')

def main(usn,pas,loop):
    for i in range(int(loop)):
        browser = Browser('/chromedriver')


        browser.open_page('https://elok.ugm.ac.id/course/view.php?id=11841')

        browser.elok(usn,pas)
        browser.open_page('https://elok.ugm.ac.id/mod/resource/view.php?id=365251')
        browser.open_page('https://elok.ugm.ac.id/mod/resource/view.php?id=364440')
        browser.open_page('https://elok.ugm.ac.id/mod/resource/view.php?id=363132')
        browser.open_page('https://elok.ugm.ac.id/mod/resource/view.php?id=362026')
        browser.open_page('https://elok.ugm.ac.id/mod/resource/view.php?id=352719')
        browser.open_page('https://elok.ugm.ac.id/mod/resource/view.php?id=354148')
        browser.open_page('https://elok.ugm.ac.id/mod/resource/view.php?id=360536')
        browser.open_page('https://elok.ugm.ac.id/mod/resource/view.php?id=361992')

        browser.close_browser()
    return reOpen.main()