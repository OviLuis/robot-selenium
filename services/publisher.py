import time

from services.web_publisher_service import WebPublisherService
from Invercol.invercol_publisher import InvercolPublisher

class Publisher:

    def __init__(self, company_name, social_media, location):
        self.company_name = company_name
        self.social_media = social_media
        self.location = location
        self.publiser_service = WebPublisherService('chrome')


    def publish_by_company(self):
        driver = publiser_service.init_driver()
        time.sleep(10)
        self.publiser_service.maximize(driver)
        if self.company_name == 'invercol':
            InvercolPublisher(driver, self.social_media, self.location)
        else:
            raise Exception ('Compañia no configurada')
