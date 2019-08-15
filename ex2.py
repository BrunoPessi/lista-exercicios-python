# 2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo, e mostre-o por extenso.
# Este número deverá variar entre 1 e 5. Se o usuário introduzir um número que não pertença a este intervalo,
# mostre a frase “número inválido”.

def numero_extenso(num):

    if num == 1:
        print("Numero por extenso: Um")
        print("Numero digitado:", num)

    elif num == 2:
        print("Numero por extenso: Dois")
        print("Numero digitado:", num)

    elif num == 3:
        print("Numero por extenso: Tres")
        print("Numero digitado:", num)

    elif num == 4:
        print("Numero por extenso: Quatro")
        print("Numero digitado:", num)

    elif num == 5:
        print("Numero por extenso: Cinco")
        print("Numero digitado:", num)

    else:
        print("Numero inválido")


num = int(input("Digite um numero:"))
numero_extenso(num)