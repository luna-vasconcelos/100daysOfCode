'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o nímero escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

Organização do código:
- Importar módulos: random e time(sleep)
- Fazer introdução do início do jogo
- Pegar o input do usuário: "Em que numero pensei? (input do usuário)"
- Declarar variável de escolha do computador pegando do random
- Declarar time.sleep para jogo ficar bonitinho
- Comparar a variável do usuário com a variável do computador
- Imprimir o resultado
'''
import random
from time import sleep

print("--"*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("--"*20)

num_jogador = int(input("Em que número pensei? "))
num_computador = random.randint(0,5)
print("PROCESSANDO...")
sleep(2)

if num_jogador == num_computador:
    print("PABABÉNS! Você conseguiu me vencer!")
else:
    print(f"PERDEU! Eu pensei no número {num_computador} e não no {num_jogador}!")
