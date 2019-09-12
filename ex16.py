# 16 - Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA e apresente o valor do volume de uma
# caixa retangular. Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.


def calculo_volume(comprimento, largura, altura):
    volume = comprimento * largura * altura
    print("O volume da caixa retangular é: ", volume)


comprimento = int(input("Digite o comprimento"))
largura = int(input("Digite a largura"))
altura = int(input("Digite a altura"))


calculo_volume(comprimento, largura, altura)
