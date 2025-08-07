# %% uma das maneiras de definir listas

idades = [28, 42, 43, 35, 29, 28, 38]
print(idades)

# %% a lista pode conter elementos diferentes
jorge = ["Jorge", "Michel", 35, True, "Casado", 20000.90]
print(jorge)

#%% para descobrir o tipo
type(jorge)

#%% como faz para acessar um elemento dentro de uma lista

#idade
print(jorge[2])

# renda
print(jorge[5])

#%% qual a soma de todos os elementos dessa lista

idades = [28, 42, 43, 35, 29, 28, 38]
print("soma idades:", sum(idades))

# nao existe muma funcao para media no python, entao usamos o len pra descobrir o tamanho, pra poder aplicar a formula depois
print("qtde idades:", len(idades))

print("media idades:", sum(idades) / len(idades))

print("menor idade:", min(idades))

#%%

jorge = ["Jorge Michel",
         35,
         True,
         "Casado",
         ["estagiário", "ux designer", "product manager", "head of product"],
         [5000, 6500, 10000, 18000, 26000],
         ["Ana", "Carol", "May"]]

print("tamanho da lista:", len(jorge))

print(jorge[6][0]) # isso é igual a:

exs = jorge[6]
primeira_ex = exs[0]
print(primeira_ex)

#%% como fazer para pegar sempre o elemento que esta na ultima posicao

tamanho = len(jorge)
pos = tamanho - 1
exs = jorge[pos]
len(exs)

jorge[pos][len(exs)-1]

#%% tem um jeito mais simples de pegar o ultimo ao inves de calcular o tamanho e colocar a ultima -1

jorge[-1][-1]

#%% fatiamento

jorge[4][2:4]

jorge[4][-2:] # essa é a melhor forma. Estamos dizendo que queremos o elemento -2 até o fim da lista

#%%

jorge[:4] #se vai comecar do comeco da lista, nao preciso colocar o 0. E a mesma coisa se aplica ao final

#%%

jorge[start : stop] # se voce ocultou o start, ele pega o comeco da lista. se ocultar o stop, ele assume que esta indo ate o final da lista

#%% como navegar na lista de tras pra frente

salarios = jorge[5]
salarios[::-1]

# a funcão completa é jorge[start : stop : step]

salarios[::2]