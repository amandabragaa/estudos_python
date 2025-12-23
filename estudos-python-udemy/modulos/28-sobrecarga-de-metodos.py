# Sobrecarga de métodos é quando uma classe tem vários métodos com o mesmo nome, mas com parâmetros diferentes.
# python não trabalha com essa sobregarca nativa, mas é possivel criar

# não preciso passar os 3 parametros, 2 já funciona
class Calculadora:
    def somar(somar, a, b, c=0):
        return a + b + c
    
calc = Calculadora()
print(calc.somar(5,5))

print(calc.somar(5,5,5))

def somar(a, b, c):
    return a + b + c


# na função normal preciso passar os 3 parametros para funcionar
calculo = somar(5, 5, )
print(calculo)