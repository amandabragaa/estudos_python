# Funções

# Funcções são blocos de código reutilizáveis que realizam 
# uma tarefa específica. Em vez de escrever o mesmo código
# varias vezes, criamos uma função e apenas a chamamos sempre necessário.

# Exemplo "real"
# Imagine que você tem que calcular o imposto de vários produtos em uma loja.
# Em vez de repetir a mesma conta várias vezes, você pode criar uma função
# chamada calcular_imposto e usá-la sempre que precisar.

# def <nome da funcao>(parametro):
# def saudacao(nome):
#     print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

# saudacao("Maria")

# # Parametro
# def saudacao(nome):
#     print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

# saudacao("Amanda")

# exemplo que fiz pra ve se realmente entendi
# def conta(valor):
#     valor = 30 + 60
#     print(f"o valor é {valor}")

# conta(0)

# Retorno de valores

def somar(a, b):
    return a + b

# chamanda a função e armazenando o resultado
resultado = somar(5, 10)
print(f"A soma é {resultado}")

# funções com varios parametro 

def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

# Chamando a função
resultado = calcular_media(8, 7, 9)
print(f"A média é {resultado:.2f}")