from .animal import Animal

class Oso(Animal):
    def __init__(self, tipo, nombre, edad, salud, felicidad, peso):
        super().__init__(tipo, nombre, edad, salud, felicidad)
        self.tipo = "Oso"
        self.salud = 10
        self.felicidad = 45
        self.peso = peso
    def buscaMiel(self):
        self.felicidad +=25
        print("Estoy buscando miel")
        return self
    def alimentacion(self):
        self.salud += 20
        self.felicidad += 35
        print("Oso comiendo")
        return self
    def display_info(self):
        print(f"Soy el oso {self.nombre}, me gusta la miel, salud {self.salud}, felicidad {self.felicidad} y peso {self.peso}") 
        return self

if __name__ == '__main__':
    try:
        oso1 = Oso("Oso", "Pooh", 25, 10, 30, 250 )
        oso1.display_info()
        oso1.alimentacion()
        oso1.display_info()
        oso1.buscaMiel()
        oso1.display_info()
    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Oso")
