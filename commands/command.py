from utils.database import Database
from utils.record import Record
from utils.attribut import Attribut

def select(db:Database,nom_table:str,*args:str):
    table = db.get_table(nom_table)
    n_db = Database()    
    
    for c in args:
        if c not in table.get_cols_name():
            raise ValueError
        
    l_type = []
    for c in args:
        for t in table.cols:
            if t.nom == c:
                l_type.append(t.data_type)

    name_table = "_".join(args)
    n_db.create_table(name_table,[Attribut(c,t) for c,t in zip(args,l_type)])
    
    n_table = n_db.get_table(name_table)
    
    for r in table.rows:
        row = Record()
        for c in args:
            row.set_value(c,r.get_value(c))
        n_table.insert(row)
        
    return n_table