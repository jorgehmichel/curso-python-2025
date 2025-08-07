#%% escreva um programa que receba uma lista de numeros de um usuario e conte quantas vezes um numero especifico aparece

lista = [1,2,3,4,5,4,2,1,2,3,2,1,2,3,4,2,1]

numero = input("Entre com um número inteiro:")
numero = int(numero)

contador = 0 # pra contar quantas vezes o numero aparece. Comecando em 0
for i in lista: # pra percorrer a lista
    if i == numero: # pra comparar se é igual ao numero inputado
        contador += 1 # pra adicionar 1 ao contador quando ele encontra um numero

print("Quantidade de", numero, ":", contador)