# União de conceitos

# Todas as estruturas podem ser usadas separadamentes, mas 
# em um programa "real", vamos unindo essas estrututras
# para criarmos os cenários que precisamos para resolver o problema

# Exemplo

# Você quer saber se uma palavra contém a letra Y

# palavra = "Python"

# for letra in palavra:
#     if letra == "y":
#         print("Essa palavra tem a letra Y!")



palavra = input("Escreva uma palavra: ")
letra = input("Escolha uma letra: ")

for abc in palavra:
    if letra == abc:
        print("Essa palavra tem a letra ", abc, "!")