from .animal import Animal

class Leon(Animal):
    def __init__(self, tipo, nombre, edad, salud, felicidad, genero):
        super().__init__(tipo, nombre, edad, salud, felicidad)
        self.tipo = "Leon"
        self.salud = 50
        self.felicidad = 40
        self.genero = genero
    def rugir(self):
        self.felicidad +=150
        print("Rugir rururururururu")
        return self
    def alimentacion(self):
        self.salud += 10
        self.felicidad +=30
        print("Comer umumumumumumum")
        return self
    def display_info(self):
        if self.genero == "masculino":
            print(f"Soy {self.nombre} el Rey de la selva, de {self.edad} anios, salud {self.salud}, felicidad {self.felicidad} y genero {self.genero}") 
        else: 
            print(f"Soy {self.nombre} La Reina hermosa de la selva, de {self.edad} anios, salud {self.salud}, felicidad {self.felicidad} y genero {self.genero}") 
        return self

if __name__ == '__main__':
    try:
        leon1 = Leon("León", "Leonina", 33, 20, 30, "femenino" )
        leon1.display_info()
        leon1.alimentacion()
        leon1.rugir()
        leon1.display_info()
    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Leon")