# 10 - receba três notas de um aluno e informe se ele passou ou reprovou.


def calcula_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3

    if media > 6:
        print("Aprovado!")
        print(media)

    if media < 6:
        print("Reprovado!")
        print(media)

notas =[]

n1 = int(input("Digite a n1: "))
n2 = int(input("Digite a n2: "))
n3 = int(input("Digite a n3: "))

calcula_media(n1,n2,n3)


