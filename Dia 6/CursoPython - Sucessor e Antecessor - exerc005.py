'''
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
# declarar o número inteiro com input, variável principal do programa
# declarar fórmulas para o antecessor e o sucessor
# imprimir resultados do sucessor e antecessor
'''

num = int(input("Digite um número inteiro: "))

ant = num - 1
suc = num + 1

print(f"Analisando o valor {num}, seu antecessor é {ant} e o seu sucessor é {suc}")
