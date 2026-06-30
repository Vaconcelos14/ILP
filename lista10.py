n = int(input())
numeros = list(map(int, input().split()))

produto = 1

for num in numeros:
    produto *= num

print(produto)
