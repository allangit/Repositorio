import pandas as pd 
import time
import numpy as np
import matplotlib.pyplot as plt 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class Mercado:

    def __init__(self):

        '''variables a extraer'''
        self.marca=0
        self.llamada=0
        self.precio=0
        self.propietario=0
        self.lugar=0
        self.year=0
        self.posting=0
        self.link=0
        self.df=0
        '''listas'''
        self.marcas=[]
        self.precios=[]
        self.propietarios=[]
        self.lugares=[]
        self.years=[]
        self.postings=[]
        self.links=[]
        self.llamadas=[]
        '''driver'''
        self.driver=webdriver.Chrome()
        self.driver.get("https://vehiculos.mercadolibre.co.cr/")

        '''inicializacion de las variables'''

        self.i=0
        self.boton=0
        self.nexct=0

    def extraer_data(self):

        self.boton=self.driver.find_element(By.XPATH,'//a[@role="button"]').get_attribute('href')
        print(self.boton)

        while self.i <4:

            '''extraer los datos'''

            self.postings=self.driver.find_elements(By.XPATH,'//a[@class="ui-search-item__group__element ui-search-link"]')
            for self.posting in self.postings:

                self.link=self.posting.get_attribute('href')
                self.links.append(self.link)

            '''Extraer los datos'''

            for self.link in self.links:

                try:

                    self.driver.get(self.link)
                    self.precio=self.driver.find_element(By.XPATH,'//span[@class="andes-money-amount__fraction"]').text
                    self.marca=self.driver.find_element(By.XPATH,'//h1[@class="ui-pdp-title"]').text
                    self.propietario=self.driver.find_element(By.XPATH,'//h3[@class="ui-pdp-color--BLACK ui-pdp-size--LARGE ui-pdp-family--REGULAR"]').text
                    self.lugar=self.driver.find_element(By.XPATH,'//p[@class="ui-seller-info__status-info__subtitle"]').text
                    self.llamada=self.driver.find_element(By.XPATH,'//p[@class="ui-seller-info__status-info__subtitle"]').text
                    '''ingresar datos lista'''
                    self.propietarios.append(self.propietario)
                    self.precios.append(float(self.precio.replace(",","")))
                    self.marcas.append(self.marca)
                    self.lugares.append(self.lugar)
                    self.llamadas.append(self.llamada)
                
                except Exception as e:

                    print(e)
                    self.driver.back()

            '''encontrando al boton para dar click'''
            self.links=[]
            self.postings=[]

            try:
                print("entro al boton")
                time.sleep(10)
                self.boton=self.driver.find_element(By.XPATH,'//span[@role="button"]')
                self.boton.click()
                time.sleep(8)
               
            except :

                pass

            self.i+=1
            self.df=pd.DataFrame(

                    {
                        'propietarios':self.propietarios,
                        'precios':self.precios,
                        'marca':self.marcas,
                        'lugares':self.lugares,
                        'llamadas':self.llamadas
                    }
            )

            print(self.df)

p=Mercado()
p.extraer_data()