quant = int(input("Digite a quantidede de itens da lista:"))
itens = input("Digite os itens da lista separados por espaço:").split()
num = [int(item) for item in itens]
par=[]
for i in num:
    if i %2 == 0:
        par.append(i)
print(len(par))

