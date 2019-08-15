# 7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois, informe o menor, número,
# o maior número, a soma dos números informados e a média aritmética dos números informados.


def maior (numeros):
    print("O maior numero digitado foi:",max(numeros))

def menor (numeros):
    print("O menor numero digitado foi:",min(numeros))

def soma(numeros):
    soma_elementos = 0
    for num in numeros:
        soma_elementos += num
    print("A soma dos numeros digitados é:", soma_elementos)

def media(numeros):
    soma_elementos = 0
    for num in numeros:
        soma_elementos += num

    media_elementos = soma_elementos/len(numeros)
    print("A media dos numeros digitados é:", media_elementos)

numeros = []

for i in range(0, 9):
    num = int(input("Digite um numero"))

    numeros.append(num)

maior(numeros)
menor(numeros)
soma(numeros)
media(numeros)