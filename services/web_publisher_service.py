from selenium import webdriver

class WebPublisherService:
    """docstring for WebPublisherService."""

    def __init__(self, browser):
        self.browser = browser

    def init_driver(self):
        # TODO hacer la implementacion para otros navegadores
        if self.browser == 'chrome':
            return webdriver.Chrome('driver//chromedriver.exe')
        else:
            raise Exception('Navegador incorrecto...')

    def maximize(self, driver):
        driver.maximize_window()
