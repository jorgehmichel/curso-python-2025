#%%

numero = input("Digite um número para descobrir a raiz quadrada")
numero = int(numero)
raiz = numero ** 0.5 #ou ** (1/2)
raiz = round(raiz, 4) #limita a quantidade de caracteres após a virgula por arredondamento

print("A raiz quadrada de", numero, "é:", raiz)