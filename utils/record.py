from typing import Dict

"""
    Représente une ligne d'une relation (équivalent d'un tuple en algèbre relationnelle).
    Stocke les valeurs sous forme {nom_colonne: valeur}.
"""

class Record():
    def __init__(self) -> None:
        self.values:Dict[str,object] = dict()
        
    def set_value(self,column_name:str,val:object):
        if not isinstance(column_name, str) or not column_name.strip():
            raise ValueError("Le nom de colonne doit être une chaîne non vide")
        self.values[column_name] = val
        
    def get_value(self,column_name:str):
        if column_name not in self.values.keys():
           raise KeyError(f"{column_name} est introuvable dans le record")
        
        return self.values[column_name]
    
    def __repr__(self):
        return f"Record({self.values})"

    def __iter__(self):
        return iter(self.values.items())

    def __eq__(self, other):
        if not isinstance(other, Record):
            return False
        return self.values == other.values
    
    def __str__(self):
        return " | ".join(f"{k}={v}" for k, v in self.values.items())

    def keys(self):
        return self.values.keys()

    def values_list(self):
        return list(self.values.values())