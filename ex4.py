# 4 - Faça um programa que receba um valor que é o valor pago, um segundo valor que é o preço do produto e retorne o
# troco a ser dado. (modifique para receber um valor de desconto e subtraia do valor do produto).

def desconto(valor_pago, valor_desconto):
    conta = valor_pago * (valor_desconto/100)
    print("Valor total com desconto: ", conta)

valor_pago = int(input("Digite o valor que foi pago: "))
valor_desconto = int(input("Digite o valor de desconto: "))

desconto(valor_pago,valor_desconto)
