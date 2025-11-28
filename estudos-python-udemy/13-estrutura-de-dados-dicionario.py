# sao dicionario no python que armazenam pares de chaves e valores 

aluno = {"nome": "Ana", 
         "idade": 24, 
         "cidade": "Rio de Janeiro"
}

# acessa a chave idade e traz o valor que está armazenado nela
print(aluno['idade'])

# adiciona um chave valor
aluno['sexo'] = "feminino"
aluno['curso'] = "Python"
print(aluno)

# deletar
del aluno['curso']
print(aluno)

for chave,valor in aluno.items():
    print(chave, ":", valor)