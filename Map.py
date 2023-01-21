import pandas as pd    
import pandas_datareader as pdr   
from folium import folium 
import streamlit as st 
from streamlit_folium import st_folium
from folium import plugins


class main_page():
    
    def __init__(self):
        self.df = pd.read_csv("datas/data.csv")

        map = folium.Map([39 ,36], zoom_start=5,width="%100",height="%100")
        location=self.df[["Lat","Lon"]]
        plugins.MarkerCluster(location).add_to(map)
        st_map = st_folium(map,height=600,width=800, zoom = 5)


main_page_instance = main_page()