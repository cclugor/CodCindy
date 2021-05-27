# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:49:50 2020

@author: cclugor
"""

from selenium import webdriver

# este argumento es para chrome trabaje de manera silenciosa
opts = webdriver.ChromeOptions()
opts.add_argument("headless")

# cargo el webdriver (descargar acá dependiendo de la versión de Chrome: 
# https://chromedriver.chromium.org/getting-started)
driver = webdriver.Chrome(executable_path = r"C:\Users\lugor\Downloads\chromedriver.exe",options=opts)

# dirección a consultar
driver.get('https://www.dolar-colombia.com/')

# dirección de la info
trm = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]")

# limpieza
trm_1=trm[0].text
trm_1=trm_1.replace(" COP", "")
trm_2=trm_1.replace(",", "")
trm=float(trm_2)
print("TRM de hoy:", trm)

# cierro el driver
driver.quit()