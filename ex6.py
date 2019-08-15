# 6 - Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar,
# e se é positivo ou negativo.

def valida_impar_par(num):
    aux = num % 2

    if aux == 0:
        print("O numero digitado: ", num, "é par!")
    else:
        print("O numero digitado: ", num, "é impar!")

def valida_positivo_negativo(num):

    if num >=0:
        print("O numero digitado: ", num, "é positivo!")
    else:
        print("O numero digitado: ", num, "é negativo!")

num = int(input("Digite o numero:"))
valida_impar_par(num)
valida_positivo_negativo(num)