#%% Faça um programa que vende garrafas de agua.

texto = """
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""
opcao = input (texto)
opcao = int(opcao)

if opcao == 1:
    print("Sua conta deu: R$ 1,50")

elif opcao == 2:
    print("Sua conta deu: R$ 2,50")

else:
    print("Entre com a porra da opção correta, por favor.")

#%% escrevendo de uma forma pra evitar retrabalho e reescrita de uma mesma mensagem

texto = """
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""
opcao = input (texto)
opcao = int(opcao)

conta = 0
if opcao == 1:
    conta = "1,50"
elif opcao == 2:
    conta = "2,50"

if conta == 0:
    print("Entre com a porra da opção correta, por favor.")
else:
    print("A sua conta é: R$", conta)