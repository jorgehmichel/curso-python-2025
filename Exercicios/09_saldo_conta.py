#%% programa que receba quantidade indefinida de valores de saldo em conta, ate entrar um valor vazio

saldo_total = 0
novo_valor = 0

while True:
    saldo = input("Entre com o saldo:")
    if saldo == "":
        break #quebra o laço
    saldo_total += float(saldo)
    
print("Saldo total:", saldo_total)