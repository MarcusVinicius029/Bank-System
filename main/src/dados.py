import random
import requests

class conta:
    operacoes = 0
    def dados(self, nome, senha, infos):
        conta = ""
        for n in range(0, 3):
            conta = conta + str(random.randrange(0, 100))

        infos[conta] = {"Nome": nome, "Senha": senha, "Saldo": 0, "Extrato": {}}
        return conta
    
    def verifica_dados(self, conta, senha, infos):
        if len(infos) == 0:
            return False
        elif conta in infos:
           if infos[conta]["Senha"] == senha:
               return True
        else:
            return False
        
    def saque(self, conta, valor, infos):
        _saldo = infos[conta]["Saldo"]
        if valor > _saldo:
            return False
        else:
            infos[conta]["Saldo"] -= valor
            self.operacoes += 1
            infos[conta]["Extrato"][f"Saque {self.operacoes}"] = valor
            return True
        
    def deposito(self, conta, valor, infos):
        _saldo = infos[conta]["Saldo"]
        if valor > 0:
            infos[conta]["Saldo"] += valor
            self.operacoes += 1
            infos[conta]["Extrato"][f"Depósito {self.operacoes}"] = valor
            return True
        else:
            return False
        
    def extrato(self, conta, dicte):
        return dicte[conta]["Extrato"]

class cotacao:
    @staticmethod
    def dolarcotacao():
        req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        _dados = req.json()
        return [_dados['USDBRL']['name'], _dados['USDBRL']['high']]
