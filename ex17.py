# 17 - Cria uma lista para armazenar 5 nomes fixos. Após inserir os 5 nome da lista mostre-os no console (utilize um
# for).

def lista():
    nomes = []
    for i in range (5):
        n = (input("Digite um nome:"))
        nomes.append(n)
    print(nomes)

lista()
