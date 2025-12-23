# Condicionais

# São estruturas que permitem ao nosso programa tomar decisões com base 
# em determinafas condições. em outras palavras, o progtama pode executar 
# ações diferentes dependendo de uma situação específica.

# Exemplo

# Você está em uma cafeteria e está com pouca grana. 
# O cappuccino custa 10 reais, café com leite 7 e o café simples 4.

# Se você tiver 10 reais ou mais na carteira, pode pedir o cappuccino.
# Se você tiver 7 reais ou mais, pode pedir o café com leite.
# Se não, pede o café simples. 

# Sintaxe básica no Python

# if - se
# else - se não
# elif - se + não 

# if condições:
    # Código a ser executado se a condição for verdadeira
# elif outra_condição:
    # Código executado se a primeira condição for falsa, mas essa for verdadeira
# esle:
    # Código executado se nenhuma das condições anteriores for verdadeira



file = int(input(f"Quantos reais você tem? "))

if file >= 10:
    print("Você pode tomar um Capppuccino")
elif file >= 7:
    print("Você pode tomar um café com leite!")
else: 
    print("Você só pode tomar um café simples")

# defaut -> vai acontecer se nada der certo, é o padrão