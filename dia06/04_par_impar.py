#%%

def par_impar(numero: int):
    if numero % 2 == 0:
        print ("É par!")
    else:
        print("É impar")
# se voce quer armazenar o resultado em algum lugar, usa-se o return. Se é só exibir, não é necessário
numero = input("Entre com um número:")
numero = int(numero)

par_impar(numero)

#%% se quiser usar o return o codigo ficaria assim

def par_impar(numero: int):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = input("Entre com um número:")
numero = int(numero)

resultado = par_impar(numero)

print("O valor", numero, "é", resultado)