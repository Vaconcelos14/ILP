n = int(input())
numeros = list(map(int, input().split()))
lista=[]
for i in numeros:
    if i %2==0:
        lista.append(i)
        maior=max(lista)
print(maior)