'''
Read four integer values named A, B, C and D. Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).
'''

A = int(input())
B = int(input())
C = int(input())
D = int(input())

Dif = A*B - C*D

print(f"DIFERENCA = {Dif}")
#outra possibilidade de impressão com str.format():
print("DIFERENCA = {}".format(Dif))