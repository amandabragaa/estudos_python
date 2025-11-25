"""Diferença prática entre for e while

    - Use for quando você já sabe quantas vezes vai repetir.

    - Use while quando não sabe quantas repetições serão necessárias."""

# for
frutas = ["banana", "melão", "ameixa"]

for fruta in frutas:
    print(fruta)

lista = [1, 2, 3, 4]

for list in lista:
    print(list)

for chave in {"nome": "Ana", "idade": 26}:
    print(chave)

for chave, valor in {"nome": "Ana", "idade": 26}.items():
    print(chave, valor)


# while

contador = 0
while contador < 6:
    print(contador)
    contador += 1

total = 0

while True:
    valor = float(input("Valor do produto (0 para finalizar): "))

    if valor == 0:
        break

    total += valor

print("Total da compra:", total)

vida = 100

while vida > 0:
    print("Você tomou dano!")
    vida -= 20

print("Game Over!")
