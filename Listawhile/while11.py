#Escreva um programa que tem como entrada um número inteiro positivo numero e imprime os múltiplos de 3 compreendidos entre 1 e numero.
numero = int(input("Digite um número inteiro positivo: "))

for i in range(1, numero + 1):
    if i % 3 == 0:
        print(i)