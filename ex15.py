# 15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valores = []


for i in range(10):
    n = int(input(f"Digite um numero ({i}): "))

    if n in valores:
        print("Valor duplicado! Não pode isso meu guerreiro")
    else:
        valores.append(n)

print("O maior valor é: ", max(valores))