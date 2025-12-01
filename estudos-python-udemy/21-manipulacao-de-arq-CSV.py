# ideal para dados tabulares
# utilizados tranferir dados em grandes volumes

import csv
# criar e escrever no aarquivo
with open("dados.csv", "w", newline="") as arquivo:
   escritor = csv.writer(arquivo)
   escritor.writerow(["Nome","Sobrenome","Idade"]) 
   escritor.writerow(["Isa","Silva",20])
   escritor.writerow(["Marta","Rosa",56])
   escritor.writerow(["Carla","Pereira",30])
   print("Arquivo geradocom sucesso")

# ler o arquivo
with open("dados.csv", "r") as arquivo:
   leitor = csv.reader(arquivo)
   for linha in leitor:
    print(linha)

#curiosidade
import pandas as pd

dataframe = pd.read_csv("dados.csv")
print(dataframe)

# manipular dados arquivos csv
with open("dados.csv", "r") as arquivo:
  leitor = csv.reader(arquivo)
  dados = list(leitor)
  print(dados)

# transformar de csv para xlsx
import pandas as pd

# ler o arquivo csv
df = pd.read_csv("dados.csv")

# salvar o DataFrame em um arquivo XLSX
df.to_excel("dados.xlsx", index=False)