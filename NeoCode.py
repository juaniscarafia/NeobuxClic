# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

rates = [str(x) for x in range(11)]
total=0
subjects=0

#Se crea una instancia de Selenium
driver = webdriver.Firefox()
driver.get('https://www.neobux.com/m/l/?vl=F46B8AFC1F223E1D6AD823644B2E6D06')

'''Buscamos los imputs del formulario de registracion
Se completan los campos con los datos del usuario
Renombrar estos tres campos con los datos personales
'''
driver.find_element_by_id("Kf1").send_keys('USUARIO')
driver.find_element_by_id("Kf2").send_keys('PASSWORD1')
driver.find_element_by_id("Kf4").send_keys('PASSWORD2')

#Buscamos el boton ingreso y le damos la orden de clickear
driver.find_element_by_id("botao_login").click()
main_window = driver.current_window_handle

# #Busco el anuncio y le doy la orden de clickear
# driver.find_element_by_id("tggi_18").click()

#Buscamos el adprice y le damos la orden de clickear
driver.find_element_by_id("ap_h").click()
#Buscamos el boton siguiente y le damos la orden de clickear
driver.find_element_by_id("nxt_bt_a").click()
