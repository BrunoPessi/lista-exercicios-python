# 5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo), se é par ou ímpar.

def verifica_numero(num):

    if num >= 0:
        print("O numero inserido é positivo")
        print(num)
    else:
        print("O numero inserido é negativo")
        print(num)

num = int(input("Digite um numero: "))
verifica_numero(num)