# herança -> herdar algo de alguem 
# uma classe pode reutilizar códico de outras

#primeira forma
# classe principal que contém caracteristicas globais
class Animal:
    def fazer_som(self):
        print("Animal fazendo barulho!")

# classe filha que esta herdando caracteristica
class Cachorro(Animal):
     def fazer_som(self):
         print("au au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau miau")

animal = Animal()
animal.fazer_som()

cachorro = Cachorro()
cachorro.fazer_som()

gato = Gato()
gato.fazer_som()

# segunda forma
class Animal:
    def fazer_som(self):
        return "Animal fazendo barulho!"


class Cachorro(Animal):
    def fazer_som(self):
        return "au au"   

class Gato(Animal):
    def fazer_som(self):
        return "Miau miau"  
    
animais = Animal()
print(animais.fazer_som())

dog = Cachorro()
print(dog.fazer_som())

cat = Gato()
print(cat.fazer_som())