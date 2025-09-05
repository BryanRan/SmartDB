#Table

from utils.attribut import Attribut
from utils.tuple import Tuple
from typing import List

class Relation:
    def __init__(self,nom:str,attr:List[Attribut]) -> None:
        self.nom = nom
        self.rows:List[Tuple] = list()
        self.cols:List[Attribut] = attr
        
    def get_cols_name(self):
        return [col.nom for col in self.cols]    
        
    def insert(self,row:Tuple):
        for col in self.cols:
            value = row.get_value(col.nom)
            if value != None and col.data_type is not type(value):
                print(f"{value} doit être de type {col.data_type}")
        self.rows.append(row)
        
    def drop(self,attr:Attribut):
        self.cols.remove(attr)
        print(f"{attr.nom} supprimé")
            
    def display(self):
        col_width = 10
        for col_name in self.cols:
            print(f"{col_name.nom:<{col_width}}", end="")
        print()
        print("-" * (col_width * len(self.cols)))

        for row in self.rows:
            for col in self.cols:
                print(f"{row.get_value(col.nom):<{col_width}}", end="")
            print()
        print()