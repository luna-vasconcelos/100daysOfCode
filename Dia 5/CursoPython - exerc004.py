'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
# Declarar a variável que será dissecada
# Imprimir o tipo da variável
# Iteração para mostrar ao usuário o que é aquela variável inserida
'''

var = input("Digite algo: ")

print("O tipo primitivo desse algo é: ", type(var))
print("É um número? ", var.isnumeric())
print("É alfabético? ", var.isalpha())
print("É alfanumérico? ", var.isalnum())
print("Está em letras maiúsculas? ", var.isupper())
print("Está em letras minúsculas? ", var.islower())
print("Está capitalizado? ", var.istitle())

print("Por hoje é só!")
