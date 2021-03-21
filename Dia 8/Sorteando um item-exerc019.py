'''
Um professor quer sortear um dos seus quatro alunos para resolver uma questão. Faça um programa que ajude ele, lendo o nome os alunos e escrevendo o nome do escolhido
# importar bibliotecas (random)
# declarar as 4 variáveis alunos 
# declarar a lista de alunos e a escolha randomizada
# imprimir resultado
'''
import random

al1 = str(input("Primeiro aluno(a): "))
al2 = str(input("Segundo aluno(a): "))
al3 = str(input("Terceiro aluno(a): "))
al4 = str(input("Quarto aluno(a): "))

lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)

print(f"O(a) aluno(a) escolhido foi: {escolhido}")
