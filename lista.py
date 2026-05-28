quant = int(input("Digite a quantidede de itens da lista:"))
itens = input("Digite os itens da lista separados por espaço:").split()
num = [int(item) for item in itens]
soma = 0
for i in num:   
    soma+=i
print(soma)