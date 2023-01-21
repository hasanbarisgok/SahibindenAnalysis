import streamlit as st
import pandas as pd   
import numpy as np
from areas import infos

class region():
    
    def __init__(self) -> None:
        
        self.data = pd.read_csv("datas/data.csv")
        
        self.data = pd.DataFrame(self.data, columns=['region','AdName','Prices Value'])
        
        self.checkbox()
        
        self.multi_chechbox()
        
        self.checkbox_for_sort()
        
        self.buttons()


    def checkbox(self):
        
        self.optionlist = list(infos.regions.keys())
        
        self.option = st.selectbox(
        'Select a Region',
        self.optionlist)

        
    def checkbox_for_sort(self):
        
        self.sort_values = st.sidebar.checkbox('Sort the list by Prices Values.')
        
        
    def virtual(self):
        
        self.data_special = self.data.loc[self.data['region'] == self.option]
        
        st.write(self.data_special)
    
        st.write(f"The Average Prices of the Selected Region: {self.option} : ", self.data_special["Prices Value"].mean())  
        
        
    def multi_chechbox(self):
        
        self.to_compare = st.multiselect(
        'Select other Regions to compare',
        self.optionlist)
        
        self.new_array = self.to_compare
        
    
    def to_compare_def(self):
        self.data_multi = self.data[self.data["region"].isin(self.to_compare)]
        
        if self.sort_values:
        
            self.data_special = self.data_special.sort_values(by='Prices Value')
        
        self.data_multi["Count"] = self.data.groupby("region")["Prices Value"].mean()
        
        st.bar_chart(
        self.data_multi,
        x="region",
        y=["Prices Value"]
    )
        
    
    def buttons(self):
    
        self.button_1 = st.button("Analyze the Region")
        
        self.button_2 = st.button("Compare the Regions")    
        
        if self.button_1:
        
            self.virtual()
        
        if self.button_2:
        
            self.to_compare_def()        
        
        
region_averages_instance = region()