class Time:
    def __init__(self, id, nome, estado):
        self.__id = id
        self.__nome = nome
        self.__estado = estado

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__estado})"


class Jogador:
    def __init__(self, id, nome, numero, id_time):
        self.__id = id
        self.__nome = nome
        self.__numero = numero
        self.__id_time = id_time

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_id_time(self):
        return self.__id_time

    def set_id_time(self, id_time):
        self.__id_time = id_time

    def __str__(self):
        return f"{self.__id} - {self.__nome} (Camisa {self.__numero}) - Time {self.__id_time}"

times = []
jogadores = []

def inserir_time():
    id = int(input("ID: "))
    nome = input("Nome: ")
    estado = input("Estado: ")
    times.append(Time(id, nome, estado))


def inserir_jogador():
    id = int(input("ID: "))
    nome = input("Nome: ")
    numero = int(input("Número: "))
    id_time = int(input("ID do time: "))
    jogadores.append(Jogador(id, nome, numero, id_time))

def listar_times():
    for t in times:
        print(t)


def listar_jogadores():
    for j in jogadores:
        print(j)

def atualizar_time():
    id = int(input("ID do time: "))
    for t in times:
        if t.get_id() == id:
            novo_nome = input("Novo nome: ")
            novo_estado = input("Novo estado: ")
            t.set_nome(novo_nome)
            t.set_estado(novo_estado)


def atualizar_jogador():
    id = int(input("ID do jogador: "))
    for j in jogadores:
        if j.get_id() == id:
            novo_nome = input("Novo nome: ")
            novo_num = int(input("Novo número: "))
            j.set_nome(novo_nome)
            j.set_numero(novo_num)

def excluir_time():
    id = int(input("ID do time: "))
    for t in times:
        if t.get_id() == id:
            times.remove(t)
            break


def excluir_jogador():
    id = int(input("ID do jogador: "))
    for j in jogadores:
        if j.get_id() == id:
            jogadores.remove(j)
            break
            
def listar_jogadores_time():
    id_time = int(input("ID do time: "))
    for j in jogadores:
        if j.get_id_time() == id_time:
            print(j)


def transferir_jogador():
    id = int(input("ID do jogador: "))
    novo_time = int(input("Novo time: "))

    for j in jogadores:
        if j.get_id() == id:
            j.set_id_time(novo_time)
            print("Transferido!")

while True:
    print("\n1 Inserir Time")
    print("2 Listar Times")
    print("3 Atualizar Time")
    print("4 Excluir Time")
    print("5 Inserir Jogador")
    print("6 Listar Jogadores")
    print("7 Atualizar Jogador")
    print("8 Excluir Jogador")
    print("9 Jogadores por Time")
    print("10 Transferir Jogador")
    print("0 Sair")

    op = input("Escolha: ")

    if op == "1":
        inserir_time()
    elif op == "2":
        listar_times()
    elif op == "3":
        atualizar_time()
    elif op == "4":
        excluir_time()
    elif op == "5":
        inserir_jogador()
    elif op == "6":
        listar_jogadores()
    elif op == "7":
        atualizar_jogador()
    elif op == "8":
        excluir_jogador()
    elif op == "9":
        listar_jogadores_time()
    elif op == "10":
        transferir_jogador()
    elif op == "0":
        break