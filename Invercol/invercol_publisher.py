
from .invercol_web_scraper import InvercolWebScraper
from services.facebook_web_publisher import FBWebPublisher

class InvercolPublisher:

    GROUPS_FILE_PATH = './config/groups.txt'
    ADVERTISEMENTS_FILE_PATH = './config/links.txt'

    def __init__(self, driver, social_media, post_location):
        self.driver = driver
        self.social_media
        self.post_location = post_location
        self.invercol_web_scraper = InvercolWebScraper(drive)
        self.base_text = self.get_base_text()

    def read_file(file_path):
        file_name = file_path
        lines = []
        with open(file_name, 'r') as file:
            lines = file.readlines()

        return lines

    def get_base_text(self):
        return '''{title}

        PRECIO {price}

        INFO AQUI \U0001F447
        {url}

        CONTACTANOS:
        \U0001F4AC WHATSAPP: https://wa.me/573117743280
        \U0001F4DETEL FIJO: 224 4270
        \U0001F4F1 CEL: 315 896 9871 / 320 681 8104
        \U0001F3E0 DIR: CALLE 31 No. 26-70 BARRIO SALESIANOS
        VISITA NUESTRA PAGINA WEB:
        \U0001F310  www.invercolbienraiz.com
        '''

    def publisher(self):
        advertisements_list = self.read_file(self.ADVERTISEMENTS_FILE_PATH)
        if self.social_media == 'fb':
            password = 'xxxx'
            user = 'xxxx'
            fb_publisher = FBWebPublisher(user, password, driver)

            if self.post_location == 'groups':
                groups_list = self.read_file(self.GROUPS_FILE_PATH)
                for index, url in enumerate(advertisements_list):
                    print('inicia publicacion.....')
                    print(dt.datetime.now())
                    print('url-->{}'.format(url))

                    data = self.invercol_web_scraper.get_data(url)
                    title = data.get('title')
                    price = data.get('price')

                    # completar el texto que se va a publicar
                    text = self.base_text.format(title=title, price=price, url=url)

                    fb_publisher.post_in_group({
                        'group_url': groups_list[index],
                        'password': password,
                        'text': text,
                        'user': user
                    })
            elif self.post_location == 'profile':
                pass
            else:
                raise Exception('Metodo de publicacion no configurado')
        else:
            raise Exception('Red Social No configurada')
