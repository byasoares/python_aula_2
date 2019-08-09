class Calculadora():

    def soma (self, n1, n2):
        return n1 + n2

    def subt (self, n1, n2):
        return n1 - n2

    def mult (self, n1, n2):
        return n1 * n2

    def divi (self, n1, n2):
        return n1 / n2

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")


operacao = input("Selecione a operacao:")
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
calc = Calculadora()

if operacao == '1':
    print(numero1, "+", numero2,"=", calc.soma(numero1,numero2))

elif operacao == '2':
    print(numero1, "-", numero2, "=", calc.subt(numero1, numero2))

elif operacao == '3':
    print(numero1, "x", numero2, "=", calc.mult(numero1, numero2))

elif operacao == '4':
    print(numero1, "/", numero2, "=", calc.divi(numero1, numero2))

#elif = else # if