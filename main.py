from particula import Particula

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p01 = Particula(1, 4, 76, 3, 8, 36, 96, 38, 23)
p02 = Particula(2, 500, 200, 500, 200, 23, 84, 25, 12)
p03 = Particula(3, 100, 200, 200, 1, 89, 23, 78, 9)
p04 = Particula(4, 7, 4, 5, 1, 87, 34, 65, 45)
administrador = Administrador()

administrador.agregar_final(p01)cd Repo
administrador.agregar_final(p02)
administrador.agregar_inicio(p03)
administrador.agregar_final(p04)
administrador.mostrar()
