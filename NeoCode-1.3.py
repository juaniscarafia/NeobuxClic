# -*- coding: utf-8 -*-
import time
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#Login web
user = raw_input('Introducir usuario: ')
password1 = raw_input('Introducir contraseña primaria: ')
password2 = raw_input('Introducir contraseña secundaria (dejar en blanco si no tiene): ')

def wait_seconds(second):
    '''Funcion de espera para los avisos y evitar errores'''
    for valor in xrange(second+1):
        sys.stdout.write("\b\b\b%2i%%" % valor)
        sys.stdout.flush()
        time.sleep(1)
    print '\n'

#rates = [str(x) for x in range(11)]
#total = 0
#subjects = 0

#Se crea una instancia de Selenium
driver = webdriver.Firefox()
driver.get('https://www.neobux.com/m/l/?vl=F46B8AFC1F223E1D6AD823644B2E6D06')
'''Buscamos los imputs del formulario de registracion.
Se completan los campos con los datos del usuario.
Renombrar estos tres campos con los datos personales.'''
driver.find_element_by_id("Kf1").send_keys(user)
driver.find_element_by_id("Kf2").send_keys(password1)
driver.find_element_by_id("Kf4").send_keys(password2)
#Buscamos el boton ingreso y le damos la orden de clickear
wait_seconds(15)
driver.find_element_by_id("botao_login").click()

id_avisos = []
id_rojos = []
purplecant = ''
orangecant = ''
graycant = ''

#Busco la cantidad de avisos lila, gris y naranja
a = driver.find_elements_by_tag_name("a")
for i in a:
    if i.get_attribute("class") == "button small2 purple":
        purplecant = i.text
    if i.get_attribute("class") == "button small2 orange":
        orangecant = i.text
    if i.get_attribute("class") == "button small2 gray2":
        graycant = i.text
size_ad = 0

if purplecant.isdigit() == True:
    size_ad+= int(purplecant)
if orangecant.isdigit() == True:
    size_ad+= int(orangecant)
if graycant.isdigit() == True:
    size_ad+= int(graycant)

#Calculo de adprice
size_adprice = size_ad * 3

#Genero los ID de los avisos lilas y de los puntos rojos a clickear
for aviso in range(6,size_ad):
    id_avisos.append('l0l'+str(aviso))
    id_rojos.append('l'+str(aviso))

#Recorro los avisos lilas y los puntos rojos para ir haciendo los clicks
red_point = 0
print driver.title
for aviso in id_avisos:
    driver.find_element_by_id(aviso).click()
    driver.find_element_by_id(id_rojos[red_point]).send_keys(Keys.CONTROL + "t")
    urlrojo = driver.find_element_by_id(id_rojos[red_point]).get_attribute("href")
    driver.get(urlrojo)
    print driver.title
    red_point+= 1
    wait_seconds(15)
    driver.find_element_by_tag_name('body').send_keys(Keys.ALT + Keys.NUMPAD1)
driver.refresh()
print 'Clicks realizados!!, quedan ', size_adprice, ' adprize.'
print 'Comienzan clics adprize en:    ',
wait_seconds(15)

#click adprize
driver.find_element_by_id("ap_h").send_keys(Keys.CONTROL + "t")
urladprize = driver.find_element_by_id("ap_h").get_attribute("href")
driver.get(urladprize)
print 'aviso: 1    ',
wait_seconds(15)
for aviso in range(1,size_adprice):
    try:
        driver.find_element_by_id("nxt_bt_a").click()
    except:
        print 'Confirmación de cierre de adprize'
        Alert(driver).accept()
        print 'Adprize cerrado'
    print 'aviso: ', aviso+1,'    ',
    wait_seconds(15)
print 'No hay más adprize, se vieron: ', size_adprice
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
driver.find_element_by_tag_name('body').send_keys(Keys.ALT + Keys.NUMPAD1)
driver.switch_to.window(driver.current_window_handle)
print 'Volvemos a los anuncios en:    ',
wait_seconds(15)
driver.refresh()
driver.find_element_by_id("t_conta").click()
print 'Adprize cliqueados'