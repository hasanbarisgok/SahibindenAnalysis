import pandas as pd
import pandas_datareader as pdr
from areas import infos

class clean_data():
    
    city_plates = infos.swapped_plates
    regions = infos.regions
    
    def __init__(self) -> None:
        self.latitude_longitude = pd.read_csv('datas/plakalar.csv')
        #self.work_all()
    
    def new_csv(self):
        self.new_data = pd.read_csv("datas/data.csv")
        
    def seperate_columns(self):
        self.new_data[['City','District']] = self.new_data.AdDate.apply(
            lambda x: pd.Series(str(x).split("\n"))
        )
        
        self.new_data[['Prices Value','Currency']] = self.new_data.Prices.apply(
            lambda x: pd.Series(str(x).split(" "))
        )
        
    def remove_unnecessary_columns(self):
        self.new_data = self.new_data.drop('Unnamed: 0',axis=1) #Removing Columns 
        self.new_data = self.new_data.drop('Prices',axis=1) #Removing Columns
        self.new_data = self.new_data.drop('Location',axis=1) #Removing Columns
        self.new_data = self.new_data.drop('AdDate',axis=1) ##Removing Columns
        
        self.new_data = self.new_data.drop_duplicates(
            subset=["AdName"]) #Removing Duplicates Rows by `Ad Name` Column
        
    def sort_columns(self):
        self.new_data = self.new_data.sort_values(['City', 'District'], ascending=(True, True))
        
    @classmethod
    def add_plate(cls,City):
       return cls.city_plates.get(City, "0")
   
    def apply(self):
        self.new_data["Plate"] = self.new_data["City"].apply(self.add_plate)
        
    
    def get_region(self,plate):
        for region, plates in clean_data.regions.items():
            if plate in list(plates):
                return region
        return "Unknown"  
        
    
    def last_process(self):
        self.new_data["Plate"] = self.new_data["Plate"].astype(int)
        
        self.new_column_names = ["Plate","City","District","AdName","Prices Value","Currency"]
        self.new_data = self.new_data.reindex(columns=self.new_column_names)
        self.new_data["region"] = self.new_data["Plate"].apply(lambda plate: self.get_region(plate))
        self.new_data.to_csv("datas/data.csv", index=False)
                   
    def add_lat_lon(self):
        self.new_data = self.new_data.merge(self.latitude_longitude[['plaka', 'lat', 'lon']], left_on='Plate', right_on='plaka', how='left')
        self.new_data.drop(columns=['plaka'], inplace=True)
        self.new_data.rename(columns={'lat': 'Lat', 'lon': 'Lon'}, inplace=True)
        self.new_data = self.new_data.dropna()
        self.new_data.to_csv("datas/data.csv", index=False)

        
        
    def work_all(self):
        self.new_csv()
        self.seperate_columns()
        self.remove_unnecessary_columns()
        self.sort_columns()
        self.apply()
        self.last_process()
        self.add_lat_lon()
  
    

clean_data_instance = clean_data()


