# -*- coding: utf-8 -*-

import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import*
import requests
import lxml

class Mercado:
    

    def __init__(self):
        

        self.driver=webdriver.Chrome()
        self.driver.get('https://listado.mercadolibre.com.ec/herramientas-vehiculos/')
        sleep(3)
        '''definir las variables a extraer'''

        self.modelo=0
        self.precio=0

        '''definir las listas '''

        self.lista_modelo=[]
        self.lista_precio=[]

        '''definir  los postings a extraer'''
        self.links_productos=[]
        self.links=0

        '''definir los postings para extraer los datos'''

        self.posting=0
        self.postings=[]

        '''definir las paginas a extraer'''

        self.i=0
        self.disclaimer=0

        '''definir los botones'''

    def extraer_data(self):
    
      try: # Encerramos todo en un try catch para que si no aparece el discilamer, no se caiga el codigo
           
        self.disclaimer = self.driver.find_element(By.XPATH, '//button[@data-testid="action:understood-button"]')
        self.disclaimer.click() # lo obtenemos y le damos click

      except Exception as e:
   
        print (e) 
        None

        '''extraer los links donde se encuentran la informacion para Robot'''

       
      while self.i <2:

        #
        self.links_productos=[]
        self.postings=0
        self.postings=self.driver.find_elements(By.XPATH,'//div[@class="ui-search-item__group ui-search-item__group--title"]')


        for self.posting in self.postings:
              
          self.links=self.posting.find_element(By.XPATH,'.//a[@class="ui-search-item__group__element ui-search-link__title-card ui-search-link"]').get_attribute('href')
          self.links_productos.append(self.links)
          print(self.links)


        for self.links in self.links_productos:
           
          try:
            
            self.driver.get(self.links)
            sleep(2)
            self.modelo=self.driver.find_element(By.XPATH,'//h1[@class="ui-pdp-title"]').text
            self.lista_modelo.append(self.modelo)
            print(self.modelo)
            self.driver.back()

          except Exception as e:
                  
            print(e)
            self.driver.back()

        try:

          print("Entro al boton")
          sleep(4)
          self.boton=self.driver.find_element(By.XPATH,'//a[@title="Siguiente"]')      
          self.boton.click()
          sleep(5)

        except Exception as e:
              
          print(e)
          break
        
        self.i+=1

      #  
m=Mercado()
m.extraer_data()

      

       





