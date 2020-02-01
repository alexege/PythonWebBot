from selenium import webdriver

class EpicBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\alexe\bin\chromedriver.exe")

    def login(self):
        self.driver.get('https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Faccount%3FsessionInvalidated%3Dtrue')
        signUpBtn = self.driver.find_element_by_xpath('//*[@id="to-register"]')
