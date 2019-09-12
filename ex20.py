# Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter  um método  aumenta_salario. Crie duas
# subclasses da classe funcionário, programador  e  analista, implementando o método  nas duas subclasses. Para o
# programador some ao atributo salário mais 20 e ao analista some ao salário mais 30,  mostrando na tela o valor.
# Depois disso, crie uma classe de testes instanciando os objetos programador e analista e chame o método
# aumenta_salario de cada um.


import unittest


class Funcionario:

    def __init__(self, salario):
        self.salario = salario

    def aumenta_salario(self):
        print("Salario aumentado!: ")


class Programador(Funcionario):

    def cargo(self):
        print("Cargo: Programador")

    def aumenta_salario(self):
        self.salario += 20
        print("Salario:", self.salario)


class Analista(Funcionario):

    def cargo(self):
        print("Cargo: Ananalista")

    def aumenta_salario(self):
        self.salario += 30
        print("Salario:", self.salario)


class Main:
    funcionario1 = Programador(800)
    funcionario1.cargo()
    funcionario1.aumenta_salario()

    funcionario2 = Analista(1000)
    funcionario2.cargo()
    funcionario2.aumenta_salario()


class TesteSalario(unittest.TestCase):

    def teste_programador(self):
        programador = Programador(800)
        resultado = programador.aumenta_salario()
        self.assertEqual(resultado, "Salario: 820")

    def teste_analista(self):
        analista = Analista(1000)
        resultado = analista.aumenta_salario()
        self.assertEqual(resultado, "Salario: 1030")
