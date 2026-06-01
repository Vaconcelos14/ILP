n = int(input())
numeros = list(map(int, input().split()))

maior = numeros[0]
segundo_maior = numeros[0]

for num in numeros[1:]:
    if num > maior:
        segundo_maior = maior
        maior = num
    elif num > segundo_maior:
        segundo_maior = num

print(segundo_maior)