#importar la bibliotecas necesarias para realizar el RPA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import lxml
import time
import cv2

class Herramientas:

    def __init__(self):

        '''definir el driver'''

        self.driver=webdriver.Firefox()
        self.driver.get("https://listado.mercadolibre.com.ec/herramientas-vehiculos/")

        '''DataFrame'''

        self.df=0
        self.i=0

        '''variables a estraer'''

        self.articulo=0
        self.boton=0

        '''lista de variables a extraer'''

        self.lista_articulos=[]

        '''nex page'''
        self.next_page=0

    def extraerData(self):


        while True:

            self.lista_postings=[]
            self.lista_links=[] 
            self.lista_postings=self.driver.find_elements(By.XPATH,'//a[@class="ui-search-item__group__element ui-search-link__title-card ui-search-link"]')

            for self.posting in self.lista_postings:

                self.link=self.posting.get_attribute('href')
                print(self.link)
                self.lista_links.append(self.link)
            
            for self.link in self.lista_links:

                try:

                    self.driver.get(self.link)
                    self.articulo=self.driver.find_element(By.XPATH,'//h1[@class="ui-pdp-title"]').text
                    print(self.articulo)
                    self.driver.back()

                except Exception as e:

                    print(e)
                    self.driver.back()
            break
p=Herramientas()
p.extraerData()