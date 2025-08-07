#%% o For percorre os elementos de um objetivo

nome = "Jorge Michel"

for letra in nome:
    print(letra)

#$$ tabuda com for

numero = 2
max_numero = 100

for i in range(1, max_numero+1): # range cria uma sequencia de numeros, de um numero inicial ate o final
    print(numero, "x", i, "=", numero * i)


#%% Quais numeros sao divisiveis por 4, no intervalo 4-100

for i in range(4, 101):
    if i % 4 == 0:
        print(i)

