# Declara funções anônimas 
# Escrever uma função mais simples/curtas
# Não consegue receber mais que um parâmetro

# Elevado ao quadrado
dobro = lambda x: x * 2
print(dobro)

# String
primeira_letra = lambda s: s[0]
print(primeira_letra("Amanda"))

ultima_letra = lambda u: u[-1]
print(ultima_letra("Lucas"))

lista = [(1,4), (2,6), (3,5)]
lista.sort(key=lambda x: x[1])
print(lista)