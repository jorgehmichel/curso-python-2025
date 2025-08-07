# %% metodos da lista

idades=[17, 42, 35, 68]
print(idades)

#%% metodo de adicionar elementos novos

idades.append(45)
print(idades)

#%% listas sao objetos mutaveis. A lista acima foi alterada, e não criada uma nova. Estamos falando do mesmo objeto

idades = []

while True:
    idade = input("Entre com a idade:")

    if idade == "":
        break
    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idade)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)


print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTDE:", qtde)