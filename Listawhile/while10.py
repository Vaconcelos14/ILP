#Escreva um programa que tem como entrada um número inteiro positivo numero e imprime os números inteiros compreendidos no intervalo [-numero; numero]
num = int(input("Digite um número inteiro positivo: "))
x=-num
while x <= num:
    print(x)
    x=x+1