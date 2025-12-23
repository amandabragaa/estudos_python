# modulos prontos
# Bibliotecas nativas do python:
# math
# radom
# os
# dateline 

# math 
import math
# usar a biblioteca pra resolver algo que queremos
print("Raiz quadrada de 16 :", math.sqrt(16))

# quando quero algo especidfico de uma biblioteca
from math import sqrt as raiz_quadrada
# print("Raiz quadrada de 16 :", sqrt(16))
print("Raiz quadrada de 16 :", raiz_quadrada(16))


# posso criar a minha propria biblioteca
# Crie um arquivo .py com suas funções e 
# importe esse arquivo em outro script 
# usando import nome_do_arquivo.