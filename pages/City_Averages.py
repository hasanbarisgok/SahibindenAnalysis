import streamlit as st
import pandas as pd   
import numpy as np
from areas import infos


class optional():
    
    def __init__(self) -> None:
        
        self.data = pd.read_csv("datas/data.csv")
        
        self.data = pd.DataFrame(self.data, columns=['City','AdName','Prices Value'])
        
        self.checkbox()
        
        self.multi_chechbox()
        
        self.checkbox_for_sort()
        
        self.buttons()
        
       
    def checkbox(self):
        
        self.optionlist = list(infos.city_plates.values())
        
        self.option = st.selectbox(
        'Select a city',
        self.optionlist)
        
        
    def checkbox_for_sort(self):
        
        self.sort_values = st.sidebar.checkbox('Sort the list by Prices Values.')
                
        
    def virtual(self):
        
        self.data_special = self.data.loc[self.data['City'] == self.option]
        
        if self.sort_values:
            self.data_special = self.data_special.sort_values(by='Prices Value')
        
        st.write(self.data_special)
        
        st.write(f"The Average Prices of the Selected City: {self.option} : ", self.data_special["Prices Value"].mean())  
        
    
    def multi_chechbox(self):
        
        self.to_compare = st.multiselect(
        'Select other cities to compare',
        self.optionlist)
        
        self.new_array = self.to_compare
        

    def to_compare_def(self):
        
        self.data_multi = self.data[self.data["City"].isin(self.to_compare)]
        
        st.bar_chart(
        self.data_multi,
        x="City",
        y=["Prices Value"]
    ) 
        
        
    def buttons(self):
        
        self.button_1 = st.button("Analyze the Region")
        
        self.button_2 = st.button("Compare the Regions")
        
        if self.button_1:
        
            self.virtual()
        
        if self.button_2:
        
            self.to_compare_def()        
        

        
    
optinal_instance = optional()
