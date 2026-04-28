class Pais:
    def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def get_nome(self):
        return self.__nome

    def get_populacao(self):
        return self.__populacao

    def get_area(self):
        return self.__area

    def set_nome(self, nome):
        if nome.strip() != "":
            self.__nome = nome
        else:
            raise ValueError("Nome inválido")

    def set_populacao(self, populacao):
        if populacao > 0:
            self.__populacao = populacao
        else:
            raise ValueError("População inválida")
    class Pais:

     def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def get_nome(self):
        return self.__nome

    def get_populacao(self):
        return self.__populacao

    def get_area(self):
        return self.__area

    def set_nome(self, nome):
        if nome.strip() != "":
            self.__nome = nome
        else:
            raise ValueError("Nome inválido")

    def set_populacao(self, populacao):
        if populacao > 0:
            self.__populacao = populacao
        else:
            raise ValueError("População inválida")
    
    def set_area(self, area):
        if area > 0:
            self.__area = area
        else:
            raise ValueError("Área inválida")

    def densidade(self):
        return self.__populacao / self.__area

class PaisUI:
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
            nome = input("Nome: ")
            populacao = int(input("População: "))
            area = float(input("Área: "))

            p = Pais(nome, populacao, area)

            print("\n--- Resultado ---")
            print("País:", p.get_nome())
            print("Densidade:", round(p.densidade(), 2), "hab/km²")

        except Exception as e:
            print("Erro:", e)

    @staticmethod
    def main():
        while True:
            op = PaisUI.menu()
            if op == 1:
                PaisUI.calculo()
            elif op == 2:
                print("Encerrando...")
                break
            else:
                print("Opção inválida")

        
        