# Listas e tuplas 

# Tipos de dados que armazazenam múltiplos valores, mas têm diferenças importantes:

# Listas:
#     - Modificávael (pode adicionar, remover e alterar valores)
#     - Mais lenta
#     - Quando precisamos modificar dados

# Tuplas:
#     - Não é moodificável (uma vez criada, não pode ser alterada)
#     - Mais rápida
#     - Quando os dados não devem ser alterados

# Listas
# Definidas entre colchetes [] e pode armazenar diferentes tipos de dados

frutas = ["banana", "maça", "pera"]
numeros = [1, 2, 3, 4, 5]
mistura = ["Python", 3.14, True]

# Acessando a lista de elementos

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1]) # índice negativo conta de trás para frente

print(frutas)

# Alterando um vallor na lista

frutas[1] = "uva"
print(frutas)

print(mistura[0])
print(mistura[1])
print(mistura[2])

# Adicionando elementos a lista

# append(): adiciona um item ao final
# insert(): adiciona um item em uma posição específica

numeros = [1, 2, 3]
print(numeros)

numeros.append(4)
print(numeros) # [1, 2, 3, 4]

numeros.insert(2, 10) # (posição, valor)
print(numeros) # [1, 2, 10, 3, 4]

# Remover elemtentos da lista

# remove(): remove um item pelo valor 
# pop(): remove um item pelo índice (ou o último item se nenhum índice for passado)

frutas = ["banana", "maça", "pera", "pitaia"]
print(frutas)

frutas.remove("maça")
print(frutas)

frutas.pop(0)
print(frutas)

frutas.pop()
print(frutas)

# Tuplas 
# Tuplas são como listas, mais imutáveis. elas são criadas com parênteses ().

cores = ("vermelho", "azul", "verde")
numeros = (1, 2, 3, 4, 5)

# Acessando elementos

print(cores[0])
print(cores[-1])

# Tentando modificar uma tupla (Erro!)
# cores[1] = "amarelo" # isso gera erro, pois tuplas são imutáveis!

# Convertendo entre lista e tupla
# Podemos converter uma tupla para uma lista e modificar os elementos

tupla = (1, 2, 3)
print(tupla)

lista = list(tupla) #Converte para lista
lista.append(4)

tupla = tuple(lista) #Converte de volta para tupla
print(tupla)

# Quando usar tuplas?
    # -Quando queremos garantir que os valores não sejam alterados.
    # -Para armazenar dados fixos como coordenadas, meses do ano, dias da semana, etc.

meses = ("Janeiro", "Fevereiro", "Março", "Abril")
print(meses[2]) #Março