n = int(input())
numeros = list(map(int, input().split()))
palpite = int(input())
if palpite in numeros:
    print("SIM")
else:
    print("NÃO")