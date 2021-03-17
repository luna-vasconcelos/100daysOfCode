'''
In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.
# declarar a linha de inserção dos valores usando a função .split para separar cada um
# declarar variáveis: 
# - codigo do produto 1 = num1
# - numero de unidades do produto 1 = uni1
# - preço de uma unidade do produto 1 = p1
# declarar o mesmo processo do produto 1 para o produto 2 = num2,uni2,p2
# declarar fórmula do total a pagar
# imprimir total a pagar
'''

linha1 = input().split()
num1 = int(linha1[0])
uni1 = int(linha1[1])
p1 = float(linha1[2])

linha2 = input().split()
num2 = int(linha2[0])
uni2 = int(linha2[1])
p2 = float(linha2[2])

val_total = uni1*p1 + uni2*p2

print("VALOR A PAGAR: R$ {:.2f}".format(val_total))
