
class Animal:
    def __init__(self, tipo, nombre, edad, salud, felicidad):
        self.tipo = tipo
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self. felicidad = felicidad
    def __str__(self):
        return f"Animal: Tipo {self.tipo}, nombre: {self.nombre}, edad: {self.edad}, salud {self.salud} y felicidad {self.felicidad}"
    def display_info(self):
        print(f"Animal: Tipo {self.tipo}, nombre: {self.nombre}, edad: {self.edad}, salud {self.salud} y felicidad {self.felicidad}") 
        return self
    def alimentacion(self):
        self.salud += 10
        self.felicidad +=10
        return self

if __name__ == '__main__':
    try:
        animal1=Animal("Animal", "peque", 25, 10, 10)
        print(animal1)
        animal1.alimentacion()
        
        animal1.display_info()
    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase animal")






