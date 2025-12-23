# Polimorfismo é a capacidade de um metodo ou objeto de se comportar de maneira diferente dependendo do contexto 

class Animal:
    def fazer_som(self):
        print("Animal fazendo barulho!")

class Cachorro(Animal):
     def fazer_som(self):
         print("au au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau") 

animais = [Cachorro(), Gato(), Animal()]
for animal in animais:
    animal.fazer_som()