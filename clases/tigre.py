from .animal import Animal

class Tigre(Animal):
    def __init__(self, tipo, nombre, edad, salud, felicidad, actividad):
        super().__init__(tipo, nombre, edad, salud, felicidad)
        self.tipo = "Tigre"
        self.salud = 20
        self.felicidad = 30
        self.actividad= 200
    def correr(self):
        self.salud +=15
        self.felicidad +=15
        self.actividad +=50
        print("Tigre corriendo")
        return self
    def alimentacion(self):
        self.salud += 20
        self.felicidad +=20
        print("El tigre comio mucho")
        return self
    def display_info(self):
        print(f"Soy un tigre llamado {self.nombre}, de {self.edad} anios, salud {self.salud}, felicidad {self.felicidad}, y actividad nivel: {self.actividad}") 
        return self

if __name__ == '__main__':
    try:
        tigre1 = Tigre("Tigre", "Tigrimmm", 33, 20, 30, 50 )
        tigre1.display_info()
        tigre1.alimentacion()
        tigre1.display_info()
        tigre1.correr()
        tigre1.display_info()
    except Exception as err:
        print("Error", err)
        print("Hay un error en la clase Tigre")