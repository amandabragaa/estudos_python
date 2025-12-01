""""
função um bloco de codigo com funcionalidades exclusivas
modularidade criar suas proprias bibliotecas ou importar de terceiros
dividir os códigos em partes menores
modularização é basicamente dividir nosso progrma em pequenas partes ou em pequenas funções
"""

# app estruturado para calcular medias dos alunos

# 1. PASSO: estruturar o progrma
    # 1. capturar notas dos alunos
    # 2. calcular a média 
    # 3. exibir o resultado

# 2. Passo: definir as funções

    # - capturar_dados()
    # - calcular_media()
    # - exibir_resultado()

# função para capturar dados 
def capturar_dados():
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)
    return notas

# função calcular media
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

# função para exibir o resultado
def exibir_resultado(media):
    if media >= 7:
        print(f"A média do aluno é {media}. Aprovado!")
    else:
        print(f"A média do aluno é {media}. Reprovado!")

notas = capturar_dados()
media = calcular_media(notas)
exibir_resultado(media)