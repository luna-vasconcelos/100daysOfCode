'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
# declarar variável numero
# declarar dobro, triplo e raiz quadrada
# imprimir resultador
'''

num = int(input("Digite um número: "))

d = num * 2 
t = num * 3 
rq = num ** (1/2)

print(f"O dobro de {num} vale {d}.")
print(f"O triplo de {num} vale {t}.")
print(f"A raiz quadrada de {num} é igual a {rq:.2f}.")
