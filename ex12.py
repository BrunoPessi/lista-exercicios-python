# 12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valores = []

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

valores.append(n1)
valores.append(n2)

if n1 == n2:
    print("Não digitar valores iguais!")
else:
    print("O maior valor é: ", max(valores))