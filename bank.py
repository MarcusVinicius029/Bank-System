import random
n = 1
start = True
usuarios = {}

def tela_inicial():
    global start
    while start:
        print("Olá, seja bem vindo!")
        print("""O que você deseja fazer?
            1-Cadastro
            2-Acessar conta
            3-Sair""")
        escolha = int(input(": "))
        if escolha == 1:
            cadastrar_usuario()
        elif escolha == 2:
            acessar_conta()
        elif escolha == 3:
            start = False



def acessar_conta():
    print("Ok, digite a sua conta e senha")
    _conta = int(input(": "))
    _senha = input(": ")
    if len(usuarios) == 0:
        print("Desculpe, mas essa conta não está cadastrado!")
        tela_inicial()
    elif usuarios.get(_conta, 00) == 00:
        print("Desculpe, mas essa conta não está cadastrado!")
        tela_inicial()
    elif usuarios[_conta] != _senha:
        print("Desculpe, senha incorreta!")
        acessar_conta()
    else:
        print(f'Seja bem vindo {usuarios[_conta]["Nome"]}')
        telaPrincipal(_conta)


def cadastrar_usuario():
    print("Olá, digite o seu nome")
    nome = input(": ")
    print(f'Ok {nome}, iremos gerar um número de conta para você:')
    conta = ""
    for x in range(0, 5):
        aleatoro = str(random.randint(0, 100))
        conta = conta + aleatoro
    print(f'O seu número de conta: {conta}')
    print("Agora crie uma senha")
    senha = input(": ")
    print("Usuário cadastrado!")
    usuarios[conta] = {"Nome": nome, "Senha": senha, "Saldo":0, "Extrato": {}}
    telaPrincipal(conta)



def depositar(_conta):
    global n
    frase2 = "Ok, digitie quanto deseja depositar!"
    print(frase2)
    _deposito = int(input("Valor: "))
    print("Depósito bem sucedido!")
    usuarios[_conta]["Extrato"][f'Operação {n}'] = f'Depósito de {_deposito} reais'
    n+=1
    usuarios[_conta]["Saldo"] = usuarios[_conta]["Saldo"] + _deposito
    telaPrincipal(_conta)

def sacar(_conta):
    global n
    frase3 = "Ok, digite quanto deseja sacar!"
    print(frase3)
    _saque = int(input("Valor:"))
    if usuarios[_conta]["Saldo"] < _saque:
        print("O valor em conta é insuficiente para completar o saque!")
        telaPrincipal(_conta)
    else:
        print("Saque bem sucedido!")
        usuarios[_conta]["Saldo"] = usuarios[_conta]["Saldo"] - _saque
        usuarios[_conta]["Extrato"][f'Operação {n}'] = f'Saque no valor de {_saque} reais'
        n+=1
        telaPrincipal(_conta)

def extrato(_conta):
    if not usuarios[_conta]["Extrato"]:
        print("Nenhuma transação registrada!")
        print(f'O seu saldo total é de {usuarios[_conta]["Saldo"]} reais')
    else: 
        for chave, valor in usuarios[_conta]["Extrato"].items():
            print(f'{chave}: {valor}')
        print(f'O seu saldo total é de {usuarios[_conta]["Saldo"]} reais')
    telaPrincipal(_conta)

def telaPrincipal(_conta):
    global start
    while start:

        frase = f"""Olá, seja bem vindo {usuarios[_conta]["Nome"]}!
        O que você deseja fazer:
        1-Depositar
        2-Sacar
        3-Obter extrato
        4-Sair"""
        print(frase)

        escolha = int(input(":"))

        if escolha == 4:
            tela_inicial()
        elif escolha == 1:
            depositar(_conta)
        elif escolha == 2:
            sacar(_conta)
        elif escolha == 3:
            extrato(_conta)


tela_inicial()
