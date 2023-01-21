from interfaces.web_publisher_interface import WebPublisherInterface
from services.fb_service import FbService



class FBWebPublisher(WebPublisherInterface):
    """docstring for FBWebPublisher."""

    def __init__(self, user, password, driver):
        super(FBWebPublisher, self).init(driver)
        self.user = user
        self.password = password

    def login(self):
        try:
            # login en facebook
            self.driver.find_element_by_xpath('//*[@id="mobile_login_bar"]/div[2]/a[1]').click()

            self.driver.find_element_by_xpath('//*[@id="m_login_email"]').send_keys(self.user)
            self.driver.find_element_by_xpath('//*[@id="m_login_password"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="login_password_step_element"]/button').click()
            time.sleep(3)
        except NoSuchElementException:
            pass

    def post(self):
        print('post on facebook')

    def open_page(self):
        self.driver.get('https://m.facebook.com')


    def post_in_group(self, group_url, text):

        # Abrir pagina de facebook
        self.open_page()

        # ir al grupo de facebook donde se creara la publicacion
        self.driver.get(group_url)

        # se loguea en caso que no lo este
        self.login()

        # dar click en el boton para crear la publicacion
        self.driver.find_element_by_xpath('//*[@id="MRoot"]/div/div[3]/div[1]/table/tbody/tr/td[2]/button').click()

        # obtener el campo de texto para incluir el texto de la publicacion
        text_element = self.driver.find_element_by_xpath('//*[@id="uniqid_1"]')

        JS_ADD_TEXT_TO_INPUT = """
          var elm = arguments[0], txt = arguments[1];
          elm.value += txt;
          elm.dispatchEvent(new Event('change'));
          """

        # adicionar el texto al campo de texto
        self.driver.execute_script(JS_ADD_TEXT_TO_INPUT, text_element, text)
        # presionar el boton enter
        text_element.send_keys(Keys.RETURN)

        # boton de publicar
        # self.driver.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[1]/div/div[3]/div/button').click()


    def post_in_profile(self, urls_list):
        self.open_page()
        self.login()
        for url in urls_list:
            seldf.post()
