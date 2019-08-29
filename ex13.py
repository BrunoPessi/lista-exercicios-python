# 13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão
# sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com
# a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.

maior_homem = 0
menor_homem = 999
maior_mulher = 0
menor_mulher = 999


def soma(maior_homem, menor_mulher):
    calculo = maior_homem + menor_mulher
    print("Homem mais velho: ", maior_homem)
    print("Mulher mais nova: ", menor_mulher)
    print("Soma do homem mais velho com a mulher mais nova: ", calculo)


def produto(menor_homem, maior_mulher):
    calculo = menor_homem * maior_mulher
    print("Homem mais novo: ", menor_homem)
    print("Mulher mais velha: ", maior_mulher)
    print("Produto do homem mais novo com a mulher mais velha: ", calculo)

homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))
mulher1 = int(input("Digite a idade da primeira mulher: "))
mulher2 = int(input("Digite a idade da segunda mulher: "))

while (homem1 == homem2) | (mulher1 == mulher2):
    print("Idades iguais não vale!")
    break

if homem1 > maior_homem:
    maior_homem = homem1
if homem2 > maior_homem:
    maior_homem = homem2
if homem1 < menor_homem:
    menor_homem = homem1
if homem2 < menor_homem:
    menor_homem = homem2

if mulher1 > maior_mulher:
    maior_mulher = mulher1
if mulher2 > maior_mulher:
    maior_mulher = mulher2
if mulher1 < menor_mulher:
    menor_mulher = mulher1
if mulher2 < menor_mulher:
    menor_mulher = mulher2


soma(maior_homem, menor_mulher)
produto(menor_homem, maior_mulher)
