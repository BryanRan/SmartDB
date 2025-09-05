#Table

from utils.attribut import Attribut
from utils.record import Record
from typing import List

class Relation:
    def __init__(self,nom:str,attr:List[Attribut]) -> None:
        if not all(isinstance(a, Attribut) for a in attr):
            raise ValueError("Tous les éléments de attr doivent être des Attributs")
        
        self.nom = nom
        self.rows:List[Record] = list()
        self.cols:List[Attribut] = attr
        
    def get_cols_name(self):
        return [col.nom for col in self.cols]    
        
    def insert(self,row:Record):
        for col in self.cols:
            value = row.get_value(col.nom)
            if value is not None and not isinstance(value, col.data_type):
                raise TypeError(f"Erreur : la valeur '{value}' pour la colonne '{col.nom}' doit être de type {col.data_type.__name__}")
        self.rows.append(row)
        
    def drop(self,attr:Attribut):
        self.cols = [col for col in self.cols if col.nom != attr.nom]
        print(f"{attr.nom} supprimé")
            
    def display(self):
        col_width = max(len(col.nom) for col in self.cols) + 2
        for col_name in self.cols:
            print(f"{col_name.nom:<{col_width}}", end="")
        print()
        print("-" * (col_width * len(self.cols)))

        for row in self.rows:
            for col in self.cols:
                print(f"{row.get_value(col.nom):<{col_width}}", end="")
            print()
        print()
        
    def __repr__(self):
        return f"<Relation {self.nom}: {len(self.rows)} lignes, {len(self.cols)} colonnes>"
