#%% escreva um programa que solicite ao usuario frases. Para para de solicitar, ele pode apenas apertar o enter.
#o programa deve apresetnar cada frase e quantas vezes ela foi repetida

dados = {}


while True:
    frase = input("Digite a sua frase:")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

for i, j in dados.items():
    print(i, "->", j)