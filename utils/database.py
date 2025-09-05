from typing import Dict,List
from utils.attribut import Attribut
from utils.relation import Relation

class Database:
    def __init__(self) -> None:
        self.database:Dict[str,Relation] = dict()
        
    def create_table(self,nom:str,cols:List[Attribut]):
        if nom in self.database.keys():
            raise ValueError(f"{nom} existe déjà!")

        self.database[nom]  = Relation(nom,cols)
        
    def get_table(self,nom:str):
        if nom not in self.database.keys():
            raise KeyError(f"{nom} n'existe pas") 
        return self.database[nom]
        
    def drop_table(self,nom:str):
        if nom not in self.database:
            raise KeyError(f"La table {nom} n'existe pas")
        del self.database[nom]
        
    def list_tables(self):
        return list(self.database.keys())
    
    def clear(self):
        self.database.clear()
        
    def __repr__(self):
        return f"<Database: {len(self.database)} tables> ({', '.join(self.database.keys())})"
