import uuid

class Client:
    def __init__(self, nome: str, cpf: str, email: str, dt_nasc: str) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__data_nascimento = dt_nasc

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self.__email

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @email.setter
    def email(self, email):
        self.__email = email

    @data_nascimento.setter
    def data_nascimento(self, dt_nasc):
        self.__data_nascimento = dt_nasc

    def __str__(self):
        return f"Olá {self.__nome} seu CPF: {self.__cpf} vinculamos ao seu email: {self.__email} sua data de nascimento foi definida {self.__data_nascimento}"


class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.banco = Banco
        self.salario = salario


class Conta_Corrente:
    def __init__(self, client: Client, saldo:float, limite:float, num_conta:str, status:enumerate):
        self.__id = str(uuid.uuid4()) #
        self.__client = client
        self.__saldo = saldo
        self.__limite = limite
        self.__num_conta = num_conta
        self.__status = status


class Conta_Poupanca:
    def __init__(self, saldo, limite, num_conta, status):
        self.client = Client
        self.saldo = saldo
        self.limite = limite
        self.num_conta = num_conta
        self.status = status


class Banco:
    def __init__(self,nome, contas: dict, ag:int, cnpj:str, funcs:dict):
        self.__nome = nome
        self.__contas = contas
        self.__ag = ag
        self.__cnpj = cnpj
        self.__funcionarios = funcs


cliente = Client("fill", "123.456.789-10", "cco@estudante.ifms.edu.br", "02/12/2000")
print(uuid.uuid4())
print(cliente)