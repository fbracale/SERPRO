class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor.nome
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante.nome
    
   
    @fabricante.setter 
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro1 = Carro('Passat')
carro2 = Carro('HB20')
carro3 = Carro('I30')
carro4 = Carro('Gol')

motor_hy = Motor('Hyundai - HY')
motor_vw1 = Motor('Volkswagen - PSS')
motor_vw2 = Motor('Volkswagen - GL')
fabricante_vw  = Fabricante('Volkswagen')
fabricante_hy = Fabricante('Hyundai')

carro1.fabricante = fabricante_vw
carro1.motor = motor_vw1

carro2.fabricante = fabricante_hy
carro2.motor = motor_hy

carro3.fabricante = fabricante_hy
carro3.motor = motor_hy

carro4.fabricante = fabricante_vw
carro4.motor = motor_vw2


print(carro1.nome, carro1.motor, carro1.fabricante)
print(carro2.nome, carro2.motor, carro2.fabricante)
print(carro3.nome, carro3.motor, carro3.fabricante)
print(carro4.nome, carro4.motor, carro4.fabricante)