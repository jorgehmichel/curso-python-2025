#%% criando uma função para calculo de juros compostos

def juros_compostos(aporte:int, taxa:float, anos:int)-> float: # não é obrigatório definir o que a variavel deve ser, mas ajuda o usuario a evitar erros
    """juros compostos serve para calcular o retorno financeiro a partir de um aporte. 
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para calculo do valor a ser retornado
    
    aporte:
    um numero inteiro, que represente o valor em reais

    taxa:
    um numero float entre 0 e 1 que represente a taxa anual

    anos:
    um numero inteiro que represente o tempo do investimento

    """
    return aporte * (1 + taxa) ** anos

#%%

juros_compostos(10000, 0.12, 4) #a ordem altera a execucao da funcao

#$$ pra evitar problemas, pode nomear o que esta declarando, assim a ordem nao importa

juros_compostos(aporte = 1000, anos = 4, taxa=0.13)