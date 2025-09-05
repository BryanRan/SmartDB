#Ligne

from typing import Dict

class Tuple():
    def __init__(self) -> None:
        self.values:Dict[str,object] = dict()
        
    def set_value(self,column_name:str,val:object):
        self.values[column_name] = val
        
    def get_value(self,column_name:str):
        if column_name not in self.values.keys():
            print(f"{column_name} introuvable")
            return
        
        return self.values[column_name]