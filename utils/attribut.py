"""
    Représente un attribut (colonne) avec un nom et un type.
    Exemple : Attribut("id", int)
"""

class Attribut():
    def __init__(self,nom:str,data_type:type) -> None:
        
        if not isinstance(nom, str) or not nom.strip():
            raise ValueError("Le nom de l'attribut doit être une chaîne non vide")
        if not isinstance(data_type, type):
            raise TypeError("data_type doit être un type Python (ex: int, str)")
        
        self.nom = nom
        self.data_type = data_type
        
    def __repr__(self):
        return f"Attribut(nom='{self.nom}', type={self.data_type.__name__})"
