def depositar(operacoes):
    frase2 = "Ok, digitie quanto deseja depositar:"
    print(frase2)
    _deposito = int(input("Valor: "))
    print("Depósito bem sucedido!")
    
    return _deposito

operacoes = {}
start = True

while start:

    usuario = {"Nome": "Marcus", "Saldo": 0}
    operacoes = []

    frase = """Olá, seja bem vindo!
    O que você deseja fazer:
    1-Depositar
    2-Sacar
    3-Obter extrato
    4-Sair"""
    print(frase)

    escolha = int(input(":"))

    if escolha == 0:
        start = False
    elif escolha == 1:
        usuario["Saldo"] = depositar()


