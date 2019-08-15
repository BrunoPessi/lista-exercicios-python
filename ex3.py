# 3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão). O
# usuário deve informar dois números e o programa deve fazer as quatro operações. (modifique para calcular tudo no
# mesmo método, somando 1 ao resultado de cada operação).

def calculadora (n1,n2):
    soma = (n1+n2) + 1
    subtrair = (n1-n2) + 1
    multiplicacao = (n1*n2) + 1
    divisao = (n1/n2) + 1

    print("\n Soma: ", soma)
    print("\n Subrtração: ", subtrair)
    print("\n Multiplicacão: ", multiplicacao)
    print("\n Divisão: ", divisao)

n1 = int(input("Digite o primero numero"))
n2 = int(input("Digite o segundo numero"))

calculadora(n1,n2)



