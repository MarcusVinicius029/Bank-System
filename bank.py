operacoes = {}
n = 1
start = True
usuario = {"Nome": "Marcus", "Saldo": 0}

def depositar():
    global n
    frase2 = "Ok, digitie quanto deseja depositar!"
    print(frase2)
    _deposito = int(input("Valor: "))
    print("Depósito bem sucedido!")
    operacoes[f'Operação {n}'] = f'Depósito de {_deposito} reais'
    n+=1
    usuario["Saldo"] = usuario["Saldo"] + _deposito
    telaPrincipal()

def sacar():
    global n
    frase3 = "Ok, digite quanto deseja sacar!"
    print(frase3)
    _saque = int(input("Valor:"))
    if usuario["Saldo"] < _saque:
        print("O valor em conta é insuficiente para completar o saque!")
        telaPrincipal()
    else:
        print("Saque bem sucedido!")
        usuario["Saldo"] = usuario["Saldo"] - _saque
        operacoes[f'Operação {n}'] = f'Saque no valor de {_saque} reais'
        n+=1
        telaPrincipal()

def extrato():
    if not operacoes:
        print("Nenhuma transação registrada!")
        print(f'O seu saldo total é de {usuario["Saldo"]} reais')
    else: 
        for chave, valor in operacoes.items():
            print(f'{chave}: {valor}')
        print(f'O seu saldo total é de {usuario["Saldo"]} reais')
    telaPrincipal()

def telaPrincipal():
    global start
    while start:

        frase = """Olá, seja bem vindo!
        O que você deseja fazer:
        1-Depositar
        2-Sacar
        3-Obter extrato
        4-Sair"""
        print(frase)

        escolha = int(input(":"))

        if escolha == 4:
            start = False
        elif escolha == 1:
            depositar()
        elif escolha == 2:
            sacar()
        elif escolha == 3:
            extrato()


telaPrincipal()
