from selenium import webdriver
import time
import datetime as dt
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


file_name = 'links_profile.txt'
urls = []
with open(file_name, 'r') as file:
    urls = file.readlines()
    # urls.append(line)


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

driver.get('https://m.facebook.com/invercolbienraiz/posts/')

driver.find_element_by_xpath('//*[@id="mobile_login_bar"]/div[2]/div/a[1]').click()
password = 'xxxxxx'
user = 'xxxxxx'
driver.find_element_by_xpath('//*[@id="m_login_email"]').send_keys(user)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="m_login_password"]').send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="login_password_step_element"]/button').click()

driver.find_element_by_xpath('//*[@id="u_0_3_IN"]').click()

# for index, url in enumerate(urls):
#     print('inicia publicacion.....')
#     print(dt.datetime.now())
#     print('url-->{}'.format(url))
#
#     # ir a la url de la propiedad a publicar
#     driver.get(url)
#     time.sleep(3)
#     #maximizar la ventana
#     driver.maximize_window()
#     time.sleep(3)
#     #obtener titulo de la propiedad
#     title = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/h2').text
#     print(title)
#     #obtener precio de la propiedad
#     price = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/h2').text
#     print(price)
#     price = price.replace(',', '.')
#     print(price)
#     time.sleep(3)
#
#     # ir al grupo de facebook
#     driver.get('https://m.facebook.com/invercolbienraiz')
#
#     time.sleep(3)
#     try:
#         # login en facebook
#         driver.find_element_by_xpath('//*[@id="mobile_login_bar"]/div[2]/div/a[1]').click()
#         password = 'LUISACOMERCIAL2022'
#         user = 'luisa940102fernanda@gmail.com'
#         driver.find_element_by_xpath('//*[@id="m_login_email"]').send_keys(user)
#         driver.find_element_by_xpath('//*[@id="m_login_password"]').send_keys(password)
#         driver.find_element_by_xpath('//*[@id="login_password_step_element"]/button').click()
#         time.sleep(3)
#     except NoSuchElementException:
#         pass
#     driver.maximize_window()
#     time.sleep(3)
#     click en boton conversacion
#     driver.find_element_by_xpath('//*[@id="MRoot"]/div/div[3]/div[1]/table/tbody/tr/td[2]/button').click()
#     time.sleep(3)
#     # obtener el campo de texto para publicar
#     text_element = driver.find_element_by_xpath('//*[@id="uniqid_1"]')
#
#
#     JS_ADD_TEXT_TO_INPUT = """
#       var elm = arguments[0], txt = arguments[1];
#       elm.value += txt;
#       elm.dispatchEvent(new Event('change'));
#       """
#
#     # completar el texto que se va a publicar
#     text = base_text.format(title=title, price=price, url=url)
#
#     # adicionar el texto al campo de texto
#     driver.execute_script(JS_ADD_TEXT_TO_INPUT, text_element, text)
#
#     #delay 3 segundos
#     time.sleep(3)
#
#     # presionar el boton enter
#     text_element.send_keys(Keys.RETURN)
#
#     #delay 3 segundos
#     time.sleep(3)
#
#     # boton de publicar
#     driver.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[1]/div/div[3]/div/button').click()
#     print('fin publicacion.....')
#     print(dt.datetime.now())
#     print('{} --> ####################################################'.format(index))
#     time.sleep(150)
