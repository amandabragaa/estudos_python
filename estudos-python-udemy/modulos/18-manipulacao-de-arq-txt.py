# TXT é uma extensão para arquivos de texto 
# as usa quando quer renomear
# \n usa quando quer quebrar a linha

# parametro w -> escrever
with open("arquivo.txt", "w") as arquivo:
    # escrever alguns dados
    arquivo.write("Linha 1: aprendendo como faz. \n")
    arquivo.write("Linha 2: aprendendo como manipula um arquivo. \n")
    arquivo.write("Linha 3: consegui compreender. \n")

    print("Dados gravados com sucesso!")


# manipulando arquivo txt
# parametro r -> ler
with open("arquivo.txt", "r") as arquivo:
    # ler o conteudo do arquivo
    conteudo = arquivo.read()
    print(conteudo) 

# apagar uma linha
with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas.pop(1))
    print(linhas)

# adicionar dados no txt
linhas = [
    "Primeira linha nova\n",
    "Segunda linha nova\n",
    "Terceira linha nova\n"
]

with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.writelines(linhas)
    print(linhas)