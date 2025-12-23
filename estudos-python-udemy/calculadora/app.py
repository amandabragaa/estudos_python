
def mostrar_terminal():
    print("A entrada não está válida!")

def verificar_input_e_digito(input):
    if input.isdigit():
        return True
    else:
        return False

def invalido():
    print("Apenas número")

def menuPrint():
    print("menu CALCULADORA")
    print("0 - SAIR")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")


try:
    while True:
        menuPrint()
        menu = input("Escolha uma opção: ")
        if verificar_input_e_digito(menu):
            print("Numero valido")
        else:
            invalido()
            continue

        menu = int(menu)
       
        if menu == 0:
            print("A operação está encerrada!")
            break
        elif menu == 1:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: ")) 
            result = num1 + num2
            print(f"O resultado da soma de {num1} e {num2} é {result}")
            
        elif menu == 2:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            result = num1 - num2
            print(f"O resultado da dubtração de {num1} e {num2} é {result}")

        elif menu == 3:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            result = num1 * num2
            print(f"O resultado da multiplicação de {num1} e {num2} é {result}")

        elif menu == 4:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            if num2 == 0:
                print("Impossível divisão por 0!")
                break
            
            result = num1 / num2
            print(f"O resultado da divisão de {num1} e {num2} é {result}")
        else:
            print("Opção inválida! Tente uma opção válida.")

        continuar = (input("Deseja continuar usando a calculadora? SIM ou NAO: "))
        if continuar == "NAO":
            break

        elif continuar == "SIM":
            print("menu CALCULADORA")
            print("0 - SAIR")
            print("1 - SOMA")
            print("2 - SUBTRAÇÃO")
            print("3 - MULTIPLICAÇÃO")
            print("4 - DIVISÃO")  

        else:
            print("❌ Digitação inválido!")
            break
except KeyboardInterrupt:
    print("\nPrograma finalizado, até mais. :D")
