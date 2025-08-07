#%% faça um programa que receba 4 alturas e realize a soma dessas alturas

soma = 0 # valor final
qtde_entradas = 4 # contador de entradas

while qtde_entradas > 0:
    altura = input("Digite uma altura para calcular a soma:")
    altura = float(altura)
    soma += altura
    qtde_entradas -= 1

print("Soma das alturas:", soma)