#%% como seria uma funcao de soma?

def soma(a:float, b:float) -> float:
    return a + b

# e uma funcão de media? 

def media(a:float, b:float)-> float:
    return soma(a, b) / 2 #pode usar a funcao de soma que ja criou antes

a = float(input("entre com o valor de a:"))
b = float(input("entre com o valor de b:"))

print("Média:", media(a,b))

#%% se quiser adicionar mais uma variavel opcional?

def soma(a:float, b:float, c=0) -> float: #o opcional tem que vir por ultimo, depois dos obrigatorios. aqui no caso o C, mas precisaria mudar outras partes do codigo
    return a + b + c #precisaria add o C aqui


def media(a:float, b:float)-> float:
    return soma(a, b, c) / 3 #aqui também e mudar o numero divisor

a = float(input("entre com o valor de a:"))
b = float(input("entre com o valor de b:"))
c = float(input("entre com o valor de c:")) #adicionar esse input também

#%% uma forma mais elegante de fazer seria

def soma(a:float,b:float,*args) -> float: #o *args significa que tudo o que passarmos na funcao sem ser valor obrigatorio, o args vai absorver. Ele é uma lista (tupla)
    valores = [a, b] + list(args) #converte o args pra uma lista. Assim voce vai estar somando duas listas (criando uma só a partir das duas)
    return sum(valores)

def media(a:float,b:float,*args)-> float:
    return soma(a, b, *args) / (len(args)+2) #pode usar a funcao de soma que ja criou antes

a = float(input("entre com o valor de a:"))
b = float(input("entre com o valor de b:"))
c = float(input("entre com o valor de c:"))
d = float(input("entre com o valor de d:"))
print("Média:", media(a, b, c,d)) #agora eu só preciso atualizar o input e o print. O args deixou o codigo pronto pra receber e trabalhar todo os inputs