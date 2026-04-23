class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2



class Circulo:
    pass

  def _init_(self, raio = 0):
    self._raio = raio

  def set_raio(self,valor):
    self._raio = valor

  def get_raio(self):
    return self._raio 

  def calc_area(self):
    return math pi * (self._raio ** 2):

  def calc_circunferencia (self)
    return 2 * math.pi * self._raio



class viagem:
    
  def _init_(self):
    self._distancia = 0
    self._tempo = 0

  def set_distancia(self, d)
    self._distancia = d
    
  def set_tempo(self,t):
    self._tempo = t

  def get_distancia(self):
    return self._tempo

  def velocidade_media(self):
    if self._tempo == 0:
        return 0
    return self._distancia / self._tempo



class ContaBancária:

  def _init_(self, titular, número):
    self._titular = titular
    self.numero = numero
    self.saldo = 0

  def depositar(self, valor):
    self._saldo += valor

  def sacar(self,valor):
    if valor <= self._saldo:
        self._saldo -= valor
    else:
        print("saldo insuficiente!")

  def get_saldo(self):
    return self._saldo

  def get_titular(self):
    return self.titular
 
  def get_numero(self):
    return self.numero



class EntradaDeCinema:

    def _init_(self, dia, hora):
        self._dia = dia.lower()
        self._hora = hora

    def calcular_valor(self):
        #preço base
        if self._dia in ["segunda", "terça", "terça", "quinta"]:
            valor = 16
        elif self._dia == "quarta":
            valor = 8
        else: #sexta,sabado,domingo
            valor = 20

        # acrescimo de 50% entre 17h e meia-noite
        if 17 <= self._hora <= 23
            valor *= 1.5


# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def triangulo():
        print("Cálculo da área do triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))     # método de instância
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        print("Em construção")

UI.main()