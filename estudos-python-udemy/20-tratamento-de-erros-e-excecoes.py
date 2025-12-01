"""
    erro
    no python não permite dividir por zero 
    pratica -> a aplicação da erro mais sa coisas não pode parar
"""
# codigo com erro porque não podemos dividir por zero
# a = 10
# b = 0
# print(a / b)

# como tratar erros/ não ideal
a = 10
b = 0

if b != 0:
    print(a / b)
else:
    print("Não é possível dividir por zero.")

# solução para tratar erros/
try :
    # código que pode gerar erro
    resultado = 10 / 0

except ZeroDivisionError:

    # o que fazer com este erro?
    print(" Erro: Não é possível dividir por zero.")

# multiplos erros 
try :
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
except ValueError :
        print(" Erro : Você deve digitar um número válido!")
except ZeroDivisionError :
        print(" Erro : Não é possível dividir por zero.")