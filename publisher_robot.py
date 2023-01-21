from selenium import webdriver
import time
import datetime as dt
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


file_name = './config/links.txt'
urls = []
with open(file_name, 'r') as file:
    urls = file.readlines()
    # urls.append(line)

g_file_name = './config/groups.txt'
groups = []
with open(g_file_name, 'r') as file:
    groups = file.readlines()
    # groups.append(line)

print(urls)
print(groups)

driver = webdriver.Chrome('driver//chromedriver.exe')
time.sleep(3)

# maximizar la ventana
driver.maximize_window()

time.sleep(3)


base_text = '''{title}

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

for index, url in enumerate(urls):
    print('inicia publicacion.....')
    print(dt.datetime.now())
    print('url-->{}'.format(url))

    # ir a la url de la propiedad a publicar
    driver.get(url)
    time.sleep(5)
    # maximizar la ventana
    # driver.maximize_window()
    # time.sleep(3)
    #obtener titulo de la propiedad
    title = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/h2').text
    print(title)
    #obtener precio de la propiedad
    price = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/h2').text
    print(price)
    price = price.replace(',', '.')
    print(price)
    time.sleep(3)
    # ir al grupo de facebook
    driver.get(groups[index])
    time.sleep(3)
    try:
        # login en facebook
        driver.find_element_by_xpath('//*[@id="mobile_login_bar"]/div[2]/a[1]').click()
        password = 'xxxx'
        user = 'xxxxx'
        driver.find_element_by_xpath('//*[@id="m_login_email"]').send_keys(user)
        driver.find_element_by_xpath('//*[@id="m_login_password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="login_password_step_element"]/button').click()
        time.sleep(3)
    except NoSuchElementException:
        pass
    driver.maximize_window()
    time.sleep(3)
    # click en boton conversacion
    driver.find_element_by_xpath('//*[@id="MRoot"]/div/div[3]/div[1]/table/tbody/tr/td[2]/button').click()
    time.sleep(3)
    # obtener el campo de texto para publicar
    text_element = driver.find_element_by_xpath('//*[@id="uniqid_1"]')


    JS_ADD_TEXT_TO_INPUT = """
      var elm = arguments[0], txt = arguments[1];
      elm.value += txt;
      elm.dispatchEvent(new Event('change'));
      """

    # completar el texto que se va a publicar
    text = base_text.format(title=title, price=price, url=url)

    # adicionar el texto al campo de texto
    driver.execute_script(JS_ADD_TEXT_TO_INPUT, text_element, text)

    #delay 3 segundos
    time.sleep(3)

    # presionar el boton enter
    text_element.send_keys(Keys.RETURN)

    #delay 3 segundos
    time.sleep(3)

    # boton de publicar
    # driver.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[1]/div/div[3]/div/button').click()
    print('fin publicacion.....')
    print(dt.datetime.now())
    print('{} --> ####################################################'.format(index))
    time.sleep(150)





def read_file():
    file_name = 'links.txt'
    urls = []
    with open(file_name, 'r') as file:
        line = file.readlines()
        urls.append(line)

def main():
    service = WebPublisherService('chrome')
    driver = service.init_driver()
    time.sleep(10)
    service.maximize(driver)
    time.sleep(10)
    fb_publisher = FBWebPublisher(driver)
    group_url = ''
    text = ''
    fb_publisher.post_group_fb(group_url, text)
    time.sleep(10)


# if __name__ == '__main__':
#     main()
