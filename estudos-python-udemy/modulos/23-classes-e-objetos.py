# reutilizar códigos
# facilitação da manuntenção
# modelagem mais intuitiva baseada no mundo real

# exemplo de ojeto : carro
class Carro:
    #função construtora
    def __init__(self, marca, modelo, ano):
        # criar objetos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# comportamento da classe carro
# instanciar os objetos  
meu_carro = Carro("hunday", "corola", 2024)
print(meu_carro.marca)
print(meu_carro.modelo)
print(meu_carro.ano)


# Exemplo conta bancária

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        #criar um objeto
        self.saldo += valor
        # transformando um texto em uma Fstring
        print(f"Depósito realizado com sucesso. Novo saldo é : R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque realizado com sucesso. Novo saldo é : R${self.saldo}")
        else:
            print("Saldo insuficiente.")

# usando a aplicação de conta bancária
minha_conta = ContaBancaria("Luciano", 3000)
minha_conta.depositar(500)
minha_conta.sacar(1000)