# Jogo de adivinhação

#  No jogo, o ussuário precisa adivinhar um número secreto.
#  Ele pode tentar várias vezes até acertar.


print("Jogo de adivinhação")
numero_correto = 6
numero = 0


while numero != numero_correto:
    numero = int(input("Digite um numero: "))
    
    if numero < numero_correto:
        print("O numero secreto é maior!")
    elif numero > numero_correto:
        print("O umero secreto é menor")
    else:
        print("Parabéns, você acertou o numero era o", numero_correto) 



