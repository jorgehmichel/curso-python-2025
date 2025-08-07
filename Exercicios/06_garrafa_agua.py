#%% 

texto = """
Escolha a sua água para comprar
(1) Água mineral natural - R$ 2,50
(2) Água mineral com gás - R$ 2,50
"""
opcao = input (texto)
opcao = int(opcao)

valor_item = 0
if opcao == 1:
    valor_item = 1.50
elif opcao == 2:
    valor_item = 2.50


if valor_item == 0:
    print("Entre com a porra da opção correta, por favor.")
else:
    
    qtde = input("Quantas garrafas?")
    qtde = int(qtde)

    valor_total = valor_item * qtde

    print("A sua conta é: R$", valor_total)
# %%
