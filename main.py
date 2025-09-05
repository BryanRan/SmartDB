from utils.attribut import *
from utils.database import *
from utils.relation import *
from utils.record import *
from commands.command import select

db1 = Database()

db1.create_table("Student",[
    Attribut("Id",int),
    Attribut("Nom",str),
    Attribut("Age",int),
    Attribut("Ville",str),
    Attribut("Filiere",str)
])

#-------------USER_TABLE---------------#

table = db1.get_table("Student")

row = Record()

row.set_value("Id", 1);
row.set_value("Nom", "Alice");
row.set_value("Age",22)
row.set_value("Ville","Paris")
row.set_value("Filiere","Informatique")

row2 = Record();
row2.set_value("Id", 2);
row2.set_value("Nom", "Bob");
row2.set_value("Age",19)
row2.set_value("Ville","Lyon")
row2.set_value("Filiere","Mathematique")

row3 = Record();
row3.set_value("Id", 3);
row3.set_value("Nom", "Claire");
row3.set_value("Age",21)
row3.set_value("Ville","Paris")
row3.set_value("Filiere","Physique")

table.insert(row)
table.insert(row2)
table.insert(row3)

print(f"Table:{table.nom}");
table.display();

table3 = select(db1,"Student","Id","Id")
print(f"Table:{table3.nom}")
table3.display()