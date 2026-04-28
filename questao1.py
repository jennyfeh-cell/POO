class Viagem:
    def __init__(self, destino, distancia, combustivel):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_combustivel(combustivel)

    def get_destino(self):
        return self.__destino

    def get_distancia(self):
        return self.__distancia

    def get_combustivel(self):
        return self.__combustivel

    def set_destino(self, destino):
        if destino.strip() != "":
            self.__destino = destino
        else:
            raise ValueError("Destino inválido")

    def set_distancia(self, distancia):
        if distancia > 0:
            self.__distancia = distancia
        else:
            raise ValueError("Distância inválida")

    def set_combustivel(self, combustivel):
        if combustivel > 0:
            self.__combustivel = combustivel
        else:
            raise ValueError("Combustível inválido")

    def consumo(self):
        return self.__distancia / self.__combustivel


class ViagemUI:
    @staticmethod
    def menu():
        try:
            print("\n1 - Calcular")
            print("2 - Fim")
            return int(input("Escolha: "))
        except:
            return 0

    @staticmethod
    def calculo():
        try:
            destino = input("Destino: ")
            distancia = float(input("Distância (km): "))
            combustivel = float(input("Combustível (L): "))

            v = Viagem(destino, distancia, combustivel)

            print("\n--- Resultado ---")
            print("Destino:", v.get_destino())
            print("Consumo:", round(v.consumo(), 2), "km/l")

        except Exception as e:
            print("Erro:", e)

    @staticmethod
    def main():
        while True:
            op = ViagemUI.menu()
            if op == 1:
                ViagemUI.calculo()
            elif op == 2:
                print("Encerrando...")
                break
            else:
                print("Opção inválida")