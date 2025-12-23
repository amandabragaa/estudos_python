# atributos são valores armazenados dentro de um objeto ou classe. Eles representam características daquele objeto e podem ser acessados sempre que o objeto for utilizado.
class Carro:
    rodas = 4 # atributos
    retrovisor = 2


carro1 = Carro() 
carro2 = Carro() 

print(carro1.rodas)
print(carro1.retrovisor)
print(carro2.rodas)

# métodos são funções dentro da classe

class Carro:
    #função construtora
    def __init__(self, marca, modelo, ano):
        # criar objetos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Método
    def acelerar(self):
        print("O carro está acelerando")

# Criando um objeto
meu_carro = Carro("Wolk", "Gol", 2024)
print(meu_carro.modelo)
print(meu_carro.marca)
print(meu_carro.ano)

# Chamando o método
meu_carro.acelerar()

