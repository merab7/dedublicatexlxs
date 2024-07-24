from abc import ABC, abstractmethod
import pandas as pd



class CarDeDublicator(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def proces_data(self):
        pass

    @abstractmethod
    def save_data(self, output_path: str):
        pass



class ToyotaDeduplicator(CarDeDublicator):
    def read_data(self):
        self.data = pd.read_excel(self.file_path)
    
    def proces_data(self):
        # names of headers columnes to ignore
        red_headers = ['Дата выпуска', 'Цвет салона', 'Цвет кузова']
        
        # making sure if the red headers exist
        existing_red_headers = [col for col in red_headers if col in self.data.columns]
        
        # droping columns with red header
        green_data = self.data.drop(columns=existing_red_headers, errors='ignore')
        
        #if all the freen rows match droping dublicates
        deduplicated_data = green_data.drop_duplicates()
        
        # setting together dedublicated green columns and ignored red columnes
        self.data = deduplicated_data.merge(self.data[existing_red_headers], left_index=True, right_index=True, how='left')

    def save_data(self, output_path: str):
        self.data.to_excel(output_path, index=False)