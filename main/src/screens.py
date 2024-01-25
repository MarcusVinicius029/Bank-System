from src.dados import *
class telaInicial:
    def __init__(self, dicte):
        self.dicte = dicte
    start = True
    def menu(self):
        print("""Olá, seja bem vindo! O que você deseja fazer?
              1 - Acessar conta
              2 - Criar conta
              3 - Sair""")
        self.entrada()
    
    def entrada(self):
        n = int(input(": "))
        if n == 1:
            p = telaAcesso(self.dicte)
            p.menu()
        elif n == 2:
            p = criarConta(self.dicte)
            p.menu()
        elif n == 3:
            self.start = False


class telaAcesso:
    def __init__(self, dicte):
        self.dicte = dicte
    def menu(self):
        print("Ok, digite a sua conta e sua senha!")
        self.entrada()

    def entrada(self):
        self._conta = input("Conta: ")
        self._senha = input("Senha: ")
        x = conta()
        i = x.verifica_dados(str(self._conta), str(self._senha), self.dicte)
        if i == True:
            p = telaPrincipal(dict, self._conta)
            p.menu(self.dicte)
        else:
            print("Desculpe, senha ou conta incorretas!")
            self.entrada()


class criarConta:
    def __init__(self, dicte):
        self.dicte = dicte

    def menu(self):
        print("""Olá, vamos criar a sua conta. Informe os dados pedidos!""")
        self.entrada(self.dicte)
    
    def entrada(self, dicte):
        self.nome = input("Nome: ")
        self.senha = input("Crie uma senha: ")
        x = conta()
        i = x.dados(self.nome, self.senha, self.dicte)
        h = telaPrincipal(self.dicte, i)
        h.menu(self.dicte)


class telaPrincipal:
    def __init__(self, dicte, conta):
        self.dicte = dicte
        self.conta = conta

    def menu(self, dicte):
        print(f"Seja bem vindo/a {dicte[self.conta]['Nome']}")
        print(f'O seu saldo é igual a {dicte[self.conta]["Saldo"]}')
        print(f'{self.conta}')
        print("""O que você deseja fazer?
              1 - Ver Cotação/Dólar
              2 - Sacar
              3 - Deposita
              4 - Ver Extrato
              5 - Sair""")
        self.entrada(dicte)
        
    def entrada(self, dicte):
        n = int(input(": "))
        if n == 1:
            i = cotacao.dolarcotacao()
            print(f'{i[0]}: {i[1]}')
            self.menu(self.dicte)
        elif n == 2:
            x = conta()
            _valor = int(input("Quanto você deseja sacar: "))
            if x.saque(self.conta, _valor, dicte):
                print("Saque realizado com sucesso!")
                self.menu(dicte)
            else:
                print("Desculpe, mas o saque não foi realizado!")
                self.menu(self.dicte)

        elif n == 3:
            x = conta()
            _valor = int(input("Quanto você deseja depositar: "))
            if x.deposito(self.conta, _valor, dicte):
                print("Depósito bem sucedido!")
                self.menu(dicte)
            else:
                print("Desculpe, mas não possível realizar o depósito!")
                self.menu(dicte)

        elif n == 4:
            x = conta()
            i = x.extrato(self.conta, dicte)
            if len(i) == 0:
                print("Extrato: Nenhuma operação registrada!")
                self.menu(dicte)
            else:
                for chave, valor in i.items():
                    print(f'{chave}: {valor}')
                self.menu(dicte)

        elif n == 5:
            x = telaInicial(dicte)
            x.menu()