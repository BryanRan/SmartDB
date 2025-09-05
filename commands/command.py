from utils.relation import Relation
from utils.database import Database
from utils.attribut import Attribut

def select(table:Relation,*args:str):
    project_table:list[Relation]  = list()
    db = Database()
    for c in args:
        if c not in table.get_cols_name():
            print(f"{c} n'existe pas da la table {table.nom}")
            return
        
    name_table = "_".join(args)
    db.create_table(name_table,[Attribut(c) for c in args])