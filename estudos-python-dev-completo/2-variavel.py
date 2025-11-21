#Váriaveis e tipos de dados "bśicos"

#Uma váriavel é um espaço na memória onde armazenamos um valor.

#<nome da var> = <valor>

#Valores definidos

nome = "Amanda"  #tipo String ("" ou '')
idade = 27       #tipo inteiro (números sem decimais)
altura = 1.76    # tipo float (número com decimais)
dev = True       # tipo booleana (True/false)

print(f"Olá, {nome}! Você tem {idade} e mede {altura}m.")

#Entrada do usuário

nome = input("Digite seu nome: ") #entrada de texto
idade = int(input("Digite sua idade: ")) # entrada de texto convertida pra int
altura = float(input("Difite sua altura: ")) #entrada convertida pra float

print(f"Olá, {nome}! Você tem {idade} e mede {altura}m.")
