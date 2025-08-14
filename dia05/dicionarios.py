#%%

lista = [2, 123, "Jorge", True, [1, 2, 3]]

lista[1]

#%% 

# dicionario são pares de chave/valor.

dados_jorge = {
                "nome":"Jorge",
                "sobrenome":"Michel",
                "filhos":False,
                "formação": ["RI", "IDE"],
                "cargos":[
                   {"nome": "ux designer", "empresa": "Itau"},
                    {"nome": "product owner", "empresa": "Itau"},
                    {"nome": "product manager", "empresa": "BV"},
                    {"nome": "product manager", "empresa": "BizCapital"}
                ]
               
}

print(dados_jorge["formação"][-1])
# as chaves devem ser string, int e float
print(dados_jorge["cargos"][-1]["empresa"])

#%% como criar uma chave nova no dicionario?

dados_jorge["estado civil"] = "casado"

#%% como descobrir os nomes das chaves ou valores de um dicionario?

dados_jorge.keys()
dados_jorge.values()
dados_jorge.items() # aqui é uma lista de tuplas que tem uma lista de chave e valor

#%%

for i in dados_jorge:
    print(i, "->", dados_jorge[i])

#%% outra forma de fazer. Usando for e passando 2 elementos ao inves de 1

for chave, valor in dados_jorge.items():
    print(chave, "->", valor)