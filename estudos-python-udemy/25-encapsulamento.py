"""
Encapsulamento é o conceito de esconder detalhes internos de uma classe e controlar como esses dados podem ser acessados.

Serve para:

- proteger atributos importantes,

- evitar que código externo altere coisas indevidas,

- organizar melhor o comportamento da classe.
"""

class Conta:
    def __init__(self,saldo):
        # quando colocamos dois underscore __ agente está dizendo que é um tributo privado
        self.__saldo = saldo

    def get_saldo(self):
        # exemplo de acesso ao saldo de forma segura
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor

# exemplo de uso
conta = Conta(1000) 
print(conta.get_saldo())  # 1000
conta.set_saldo(2000) # altera o saldo
print(conta.get_saldo()) # imprime o resultado