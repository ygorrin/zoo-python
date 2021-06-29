from clases.leon import Leon
from clases.oso import Oso
from clases.tigre import Tigre

class Zoo:
    def __init__(self, zoo_name):
        self.animales = []
        self.nombre = zoo_name

    def add_leon(self, animal):
        self.animales.append(animal)
    def add_tigre(self, animal):
        self.animales.append(animal)
    def add_oso(self, animal):
        self.animales.append(animal)
    def print_all_info(self):
        print("-"*30, self.nombre, "-"*30)
        for animal in self.animales:
            animal.display_info()

oso1 = Oso("Oso", "Pooh", 25, 10, 30, 250 )
oso1.alimentacion()
oso1.buscaMiel()
oso1.display_info()

tigre1 = Tigre("Tigre", "Tigrimmm", 33, 20, 30, 50 )
tigre1.alimentacion()
tigre1.correr()
tigre1.display_info()

leon1 = Leon("León", "Leonina", 33, 20, 30, "femenino" )
leon1.alimentacion()
leon1.rugir()
leon1.display_info()

zoo1 = Zoo("Yamy Zoo")
zoo1.add_leon(leon1)
zoo1.add_tigre(tigre1)
zoo1.add_oso(oso1)
zoo1.print_all_info()