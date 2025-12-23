# Laços de Repetições (for e while)

# Imagine que você precisa pedir para alguém contar de 1 a 100
#  e escrever cada número em um papel. Fazer isso manualmente
# seria muito cansativo e demorado.

# Agora, imagine que um pode fazer essa contagem automaticamente,
# sem precisar repitir o mesmo comando 100 vezes. É exatammento isso
# que os laços de repetições fazem!

# Os laços de repetições são usados para executar um bloco de código
# várias vezes, até que uma condição seja atingida.

# Python tem dois tipos principais de laços:
# for -> Quando sabemos quantas vezes queremos repetir algo.
# while -> Quando queremos repetir algo até que uma condição se torne falsa 

# FOR
# O for é usado quando sabemos quantas vezes queremos um bloco de código.
# Ele percorre uma sequência de valores, como uma lista, um intervalo de números
# ou até mesmo letras de uma palavra.
 
# Estrutura
 
# for variavel in sequencia:
    # Cóodigo a ser repetido

# Contando de 1 a 5 com o for

for numero in range(1,6):
    print(numero)

# O range(1,6) gera os números de 1 a 5, o último número do range não é incluido


# Percorrendo uma lista de compras

compras = ["Arroz", "Feijão", "Leite", "Ovos"]
for item in compras:
    print(f"Comprar: {item}")

# percorrendo letras

palavra = "Amanda"

for letra in palavra:
    print(letra)

# WHILE

# O while é usado quando não sabemos quantas vezes a repetição vai acontecer,
# mas sabemos a condição que deve ser atendida para continuar.
 
# while condição:
#   Código a ser repetido enquando a condição for verdadeira
 
# obs: Cuidade com loops infinitos!
# Se a condição nunca mudar para False, o código nunca para de rodar.
 
# Contagem regressiva
 
contador = 5

while contador > 0:
    print(contador)
    contador -= 1 

print("Fogo")

contador = 0

while contador < 5:
    print(contador)
    contador += 1 

print("Fogo")

# Pedindo senha até acertar

senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Acesso permitido")