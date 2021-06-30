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

# ------------Creación de instancias manuales --------------------
#oso1 = Oso("Oso", "Pooh", 25, 10, 30, 250 )
#oso1.alimentacion()
#oso1.buscaMiel()
#oso1.display_info()
#
#tigre1 = Tigre("Tigre", "Tigrimmm", 33, 20, 30, 50 )
#tigre1.alimentacion()
#tigre1.correr()
#tigre1.display_info()
#
#leon1 = Leon("León", "Leonina", 33, 20, 30, "femenino" )
#leon1.alimentacion()
#leon1.rugir()
#leon1.display_info()
#
#zoo1 = Zoo("Yamy Zoo")
#zoo1.add_leon(leon1)
#zoo1.add_tigre(tigre1)
#zoo1.add_oso(oso1)
#zoo1.print_all_info()

# ------------Interactividad --------------------

print(f"\n\nBienvenido al Zoologico")
listaZoo=[]
while True:
    print(f"\nMenu de opciones")
    print(f"Seleccione una opcion:  \n1.Crear un Zoo  \n2.Registrar un Oso  \n3.Registrar un tigre\n4.Registrar un Leon \n5.Mostrar animales del Zoo \n0.Salir")
    n = int(input("Ingresa tu opcion: "))
    
    if n == 1:
        nombre = input("\nNombre del Zoo: ")
        zoo = Zoo(nombre)
        print("\nCreaste el zoologico: ", nombre)
        listaZoo.append(zoo)

    if n == 2:
        nombre = input("\nNombre del Oso: ")
        edad = int(input("Edad: "))
        peso = int(input("Peso: "))
        oso = Oso(0, nombre, edad, 0, 0, peso)
        oso.buscaMiel()
        oso.display_info()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_oso(oso)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 3:
        nombre = input("\nNombre del Tigre: ")
        edad = int(input("Edad: "))
        tigre = Tigre(0, nombre, edad, 0, 0, 0)
        tigre.display_info()
        tigre.alimentacion()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_tigre(tigre)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 4:
        nombre = input("\nNombre del Leon: ")
        edad = int(input("Edad: "))
        gen = input("Genero F/M: ")
        if gen=="F" or gen == "f":
            genero = "femenino"
        elif gen=="M" or gen == "m":
            genero = "masculino"
        else:
            print("Error de Seleccion")
        leon = Leon(0, nombre, edad, 0, 0, genero)
        leon.display_info()
        leon.alimentacion()
        nombre_zoo = input("Ingresa el nombre del zoologico para el animal: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.add_leon(leon)
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 5:
        nombre_zoo = input("Ingresa el nombre del zoologico para ver los animales: ")
        for zoologico in listaZoo:
            if zoologico.nombre == nombre_zoo:
                zoologico.print_all_info()
            else:
                print("No se encontró el zoologico con ese nombre")

    if n == 0 :
        print("Hasta luego")
        break