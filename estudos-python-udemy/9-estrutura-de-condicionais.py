# idade = int(input("Qual a sua idade? "))

# if idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

idade = int(input("Qual a sua idade? "))

if idade <= 15:
    print("Sinto muito. Como você é de menor, não pode entrar na festa.")
elif idade <= 17:
    print("Você pode entrar na festa e não pode tomar bebidas alcoolicas.")
else:
    print("Você pode entrar na festa e tomar bebidas alcoolicas.")

vida = 35

if vida >= 70:
    print("Personagem saudável.")
elif vida >= 30:
    print("Personagem ferido, cuidado!")
else:
    print("Personagem crítico! Busque cura.")