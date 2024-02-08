from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import lxml
import time


class data:

    def __init__(self):
        
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.postings=0
        self.posting=0
        self.links=[]
        self.page=0
        self.link=0
        self.i=0
        self.boton=0
        self.boton2=0
        self.opts = Options()
        self.service=0
        self.df=0
        self.foto=0
        self.box=0
        #self.opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

    def extraer_data(self):

        while True:
        
            #boton dentro de try except 
            try:
                self.box=self.driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]')
                self.box.send_keys('perro')
                time.sleep(4)
                self.boton=self.driver.find_element(By.XPATH,'//input[@class="gNO89b"]')
                self.boton.click()
                time.sleep(10)
                self.boton2=self.driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
                self.boton2.click()
                time.sleep(10)
                self.driver.execute_script('window.scrollTo(0,38500)')
                self.postings=self.driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
                self.boton=self.driver.find_element(By.XPATH,'//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input')
                for self.posting in self.postings:
                    #especifica la carpeta donde quiere save imagenes
                    self.foto=self.posting.screenshot(r'C:\Users\desca\OneDrive\Escritorio\imagen\ '+str(self.i) + '.png')
                    self.i+=1
            except:

                break

auto=data()
auto.extraer_data()