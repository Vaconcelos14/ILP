n = int(input())
numeros = list(map(float, input().split()))
soma=0
for i in numeros:
    if i > 0:
        soma+=1
print(soma)