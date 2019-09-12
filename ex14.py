# 14 - Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).

tabuada=int(input("Tabuada do numero: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))