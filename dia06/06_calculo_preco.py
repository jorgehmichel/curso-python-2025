#%% calcular o imposto. Criando uma funcao que recebe o preco de venda de um produto e o valor do imposto em cima dele

def calc_imposto(preco:float, tx_base:float, **kwargs): #diferentemente dos *args, o **kawrgs é um dicionario
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto


#%%

calc_imposto(100, 0.03, municipio = 0.03, estadual = 0.05)# entao o kwargs é uma forma de passar valores nomeaveis pra usar depois

#%% essa é outra forma de fazer o que fizemos aqui acima:

impostos_gerais = {
    "municipio" : 0.03, 
    "estadual" : 0.05
}

calc_imposto(100, 0.03, **impostos_gerais)