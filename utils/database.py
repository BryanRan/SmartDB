from typing import Dict,List
from utils.attribut import Attribut
from utils.relation import Relation

class Database:
    def __init__(self) -> None:
        self.database:Dict[str,Relation] = dict()
        
    def create_table(self,nom:str,cols:List[Attribut]):
        if nom in self.database.keys():
            print(f"{nom} existe déjà!")
            return

        self.database[nom]  = Relation(nom,cols)
        
    def get_table(self,nom:str):
        if nom not in self.database.keys():
            print(f"{nom} n'existe pas")
            return 
        
        return self.database[nom]
        