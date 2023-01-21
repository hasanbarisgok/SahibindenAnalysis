from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd # read csv, df manipulation
from time import sleep
import streamlit as st
from cleaning import clean_data



class Scraper():
    
    car_name = st.text_input("Car Name:", placeholder='Example: Renault Fluence',max_chars=20)

    page_num = st.number_input("Page Num:",min_value=2,max_value=5,step=1)

    
    def __init__(self):
                    
        
        self.titles_list = []
        
        self.prices_list = []
        
        self.location_list = []
        
        self.date_list = []
        
        self.start_scraping()
        self.start_cleaning()
    
    @classmethod    
    def sep_car_name(cls):
        return cls.car_name.replace("",'+')
    
    
    def start_scraping(self):
        
        self.button = st.button("Start Data Scraping")
        
        if self.button:
            st.warning("The Data Scraping has started now. Please be Patient", icon = "⚠️")
            self.sep_car_name()
            self.web_driver()
            self.surfing()
            self.create_data()
            
            
    def start_cleaning(self):
        self.button_clean = st.button("Start Data Cleaning")
        
        if self.button_clean:
            self.clean = clean_data()
            self.clean.work_all()
            st.warning("The Data Cleaning Process is OK. You can see the Resuls. Thx for using!", icon = "🔥")
        
        
    
    def web_driver(self):
        self.options = Options()
        
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        
        self.driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
        
    def surfing(self):
        
        for i in range(1,self.page_num):
            self.offset = i * 50
            self.url = f'https://www.sahibinden.com/vasita?pagingOffset={i*50}&pagingSize=50&query_text_mf=renault+fluence&query_text={Scraper.car_name}'
            self.driver.get(self.url)
            sleep(4)
            
            self.item_titles = self.driver.find_elements(By.CLASS_NAME,'searchResultsTitleValue ')
            self.item_prices = self.driver.find_elements(By.CLASS_NAME,'searchResultsPriceValue')
            self.item_location = self.driver.find_elements(By.CLASS_NAME,'searchResultsDateValue')
            self.item_date = self.driver.find_elements(By.CLASS_NAME,'searchResultsLocationValue')
            
            for title in self.item_titles:
                self.titles_list.append(title.text)

            for price in self.item_prices:
                self.prices_list.append(price.text)
            
            for location in self.item_location:
                self.location_list.append(location.text)
                
            for date in self.item_date:
                self.date_list.append(date.text)
                
        self.driver.quit()
    
    def create_data(self):
        self.data = {'AdName' : self.titles_list, 'Prices' : self.prices_list, 'Location': self.location_list, 'AdDate' : self.date_list}
        self.data_new = pd.DataFrame(self.data).to_csv("datas\data.csv")
     

abc = Scraper()