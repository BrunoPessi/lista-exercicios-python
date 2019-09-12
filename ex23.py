# Crie uma programa que recebe uma lista qualquer e:
# a. retorne o maior elemento
# b. retorne a soma dos elementos
# c. retorne o número de ocorrências do primeiro elemento da lista
# d. retorne a média dos elementos

def maior_elemento(lista):
    print("O maior numero digitado foi: ", max(lista))

def soma_elemento(lista):
    soma = 0
    for num in lista:
        soma += num
    print("A soma dos numeros digitados é:", soma)

def ocorrencia(lista):
    print(f"O primeiro valor ocorre {lista.count(lista[0])} vezes.")

def media(lista):
    soma_elementos = 0
    for num in lista:
        soma_elementos += num

    media_elementos = soma_elementos/len(lista)
    print("A media dos numeros digitados é:", media_elementos)


lista = []

for i in range (10):
    num = int(input(f"Insira um numero {i}: "))
    lista.append(num)


maior_elemento(lista)
soma_elemento(lista)
ocorrencia(lista)
media(lista)
