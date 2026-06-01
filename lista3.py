n = int(input())
numeros = list(map(int, input().split()))

menor = numeros[0]
maior = numeros[0]

for num in numeros:
    if num < menor:
        menor = num

    if num > maior:
        maior = num

print(menor, maior)