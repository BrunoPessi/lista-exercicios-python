# # 1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não. Receba os dados
# pela console e chame este método. (modifique este exercício para receber 5 alunos, 3 notas para cada um e calcule a
# media mostrando se está aprovado ou não)

def calcula_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3

    if media > 6:
        print("Aprovado!")
        print(media)

    if media < 6:
        print("Reprovado!")
        print(media)



notas = []

for i in range(0, 4):
    n1 = int(input("Digite sua n1"))
    n2 = int(input("Digite sua n2"))
    n3 = int(input("Digite sua n3"))

    notas.append(n1)
    notas.append(n2)
    notas.append(n3)

    calcula_media(n1,n2,n3)