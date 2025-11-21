# Simulador de caixa eletrônico

# O usuário tem um saldo inicial de R$500 e pode
# sacar dinheiro até zerar o sálario ou encerrar. 

saldo_inicial = 500


while saldo_inicial > 0:
    saque = float(input("Informe o valor do saque (ou digite 0 para sair): "))

    if saque == 0:
        break
    elif saque > saldo_inicial:
        print("Saldo insuficiente! Saque não efetuado")
    else:
        saldo_inicial -= saque
        print(f"Você tem {saldo_inicial:.2f} reais!")

print("Operação finalizada")