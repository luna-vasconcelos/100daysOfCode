'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- Quantas letras ao todo (sem considerar espaços)
- Qual é e quantas letras tem o primeiro nome
- Qual é e quantas letras tem o último nome
'''

nome = str(input("Digite o seu nome completo: ")).strip() #o strip irá eliminar os espaços inúteis antes e depois do nome

print("Analisando seu nome...")
print(f"Muito prazer em te conhecer {nome.split()[0]}!")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras")
print(f"Seu último nome é {separa[len(separa) - 1]} e ele tem {len(separa[len(separa) - 1])} letras") #o len menos 1 porque o len pega a partir do 1, mas a lista começa no 0
