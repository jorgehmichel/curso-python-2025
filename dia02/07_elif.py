#%%

idade = input("Qual é a sua idade?")
idade = int(idade)

if idade >= 70:
    print("Cuidado com a bebida.")

elif idade >= 18:
    print("Você pode beber cerveja")

elif idade == 17:
    print("Você ainda não pode, mas está quase")

else:
    print("Você não pode beber")

