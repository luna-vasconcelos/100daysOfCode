'''
Write a program that reads an employee's number, his/her worked hours number in a month and the amount he received per hour. Print the employee's number and salary that he/she will receive at end of the month, with two decimal places.
    - Don’t forget to print the line's end after the result, otherwise you will receive “Presentation Error”.
    - Don’t forget the space before and after the equal signal and after the U$.
# declarar variáveis:
 - employee's number
 - worked hours in a month
 - salary per hour
# declarar salary no mês com fórmula
# imprimir employee's number
# imprimir salary no mês
'''

emp_numb = int(input())
hrs_month = int(input())
amnt_hour = float(input())

salary = hrs_month * amnt_hour

print("NUMBER = {}".format(emp_numb))
print("SALARY = U$ {:.2f}".format(salary))
