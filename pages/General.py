import pandas as pd    
import pandas_datareader as pdr   
from folium import folium 
import streamlit as st 
from streamlit_folium import st_folium
from folium import plugins
import pydeck as pdk
import numpy as np
import plotly.figure_factory as ff

class by_city():
    
    def __init__(self):
    
        self.chart_data = pd.read_csv("datas/data.csv")
        
        self.chart_data = self.chart_data[["Plate","City","District","AdName","Prices Value","Currency","region"]]
        
        self.all_prices()
        
        self.average_prices()
        
        self.layout()
    
    
    def layout(self):
        
        self.list_button = st.sidebar.button("See the Data Table")
        
        self.prices_sorted_list_checkbox = st.sidebar.checkbox("Sort the Data Table by Prices Values.")
        
        self.city_sorted_list_checkbox = st.sidebar.checkbox("Sort the Data Table by City")
        
        self.region_sorted_list_checkbox = st.sidebar.checkbox("Sort the Data Table by Region ")
        
        if self.list_button:
        
            if self.prices_sorted_list_checkbox:
                
                self.chart_data = self.chart_data.sort_values(by='Prices Value')
           
            if self.city_sorted_list_checkbox:
                
                self.chart_data = self.chart_data.sort_values(by='Plate')
           
            if self.region_sorted_list_checkbox:
                
                self.chart_data = self.chart_data.sort_values(by='region')
                    
            if self.city_sorted_list_checkbox and self.prices_sorted_list_checkbox:
                
                self.chart_data = self.chart_data.sort_values(by=['Plate','Prices Value'])
                
            if self.city_sorted_list_checkbox and self.prices_sorted_list_checkbox:
                
                self.chart_data = self.chart_data.sort_values(by=['region','Prices Value'])     
            
            self.list()


    def all_prices(self):
        
        #All Prices for every Cities     
        
        st.write("All Pricess:")
        tooltip=['left:City', 'right:Prices Value']
        st.line_chart(
            self.chart_data,
            x="City",
            y=["Prices Value"]
        )

    
    def average_prices(self):
    
        #Average Prices for every cities
        
        st.write("Average of Prices:")
        self.averages_cities = self.chart_data.groupby('City')['Prices Value'].mean()
        tooltip=['left:City','right:Prices']
        st.line_chart(self.averages_cities)


    def list(self):
        
        st.write(self.chart_data)

city_averages_instance = by_city()