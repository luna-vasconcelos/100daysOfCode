'''
Make a program that reads a seller's name, his/her fixed salary and the sale's total made by himself/herself in the month (in money). Considering that this seller receives 15% over all products sold, write the final salary (total) of this seller at the end of the month , with two decimal places.
# declarar variáveis:
 - seller's name
 - salary
 - sale's total in the month
# declarar salary no mês com fórmula considerando os 15% em cima do vendido
# imprimir salary final do mês
'''

s_name = input()
salary = float(input())
t_sold = float(input())

f_salary = salary + t_sold*0.15

print("TOTAL = R$ {:.2f}".format(f_salary))
