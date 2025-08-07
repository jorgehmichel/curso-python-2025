#%% faça um programa que receba 4 alturas e realize a soma dessas alturas

soma = 0 # valor final
qtde_entradas = 4 # contador de entradas

for i in range(qtde_entradas): #se nao colocarmos nada entre viruglas (declarar o começo), ele vai startar o range do 0
    altura = input("Digite uma altura para calcular a soma:")
    altura = float(altura)
    soma += altura

print("Soma das alturas:", soma)