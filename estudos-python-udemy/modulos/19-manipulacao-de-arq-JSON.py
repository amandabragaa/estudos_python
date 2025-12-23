# segue uma formatação especifica para poder estruturar dados
# leve e facil cmpreensão 
# estrutura -> {chave : valor }

{
    "nome": "Joana",
    "idade": 48,
    "cidade": "São Paulo",
    "cidades_visitadas": ["RJ", "MG", "BH"]
}

import json
# criando nosso json
dados = {
    "nome": "Joana",
    "idade": 48,
    "cidade": "São Paulo",
    "cidades_visitadas": ["RJ", "MG", "BH"]
}

# colocar o caminho onde será salvo
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)
print("Arquivo JSON criado com sucesso")

# ler dados
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)

# adicionar dados no json
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    dados["cidades_visitadas"].append("SC")
    print(dados)

# salva dados
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo)

# remover o dado desejado
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    dados["cidades_visitadas"].remove("MG")
    print(dados)
