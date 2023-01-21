class InvercolWebScraper:

    def __init__(self, driver):
        self.driver = driver


    def get_data(self, url):

        # Open a new window
        self.driver.execute_script("window.open('');")

        # Switch to the new window and open new URL
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)

        #maximizar la ventana
        self.driver.maximize_window()

        #obtener titulo de la propiedad
        title = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/h2').text
        print(title)

        #obtener precio de la propiedad
        price = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/h2').text
        price = price.replace(',', '.')
        print(price)

        return {'title': title, 'price': price}
