'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o nímero escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

Organização:
- Importar módulos: random e time(sleep)
- Declarar dicionário de cores
- Fazer introdução do início do jogo
- Estrutura de repetição para o jogo continuar até o jogador escolher parar
- Pegar o input do usuário: "Em que numero pensei? (input do usuário)"
- Declarar variável de escolha do computador pegando do random
- Declarar time.sleep para jogo ficar bonitinho
- Estrutura condicional para comparar a variável do usuário com a variável do computador
- Imprimir o resultado
'''
import random
from time import sleep
cores = { #estrutura de dicionário com as cores na tabela ANSI usadas no programa 
    'limpa' : '\33[m',
    'amarelo' : '\33[33m',
    'verde' : '\33[0;32m',
    'magenta' : '\33[1;95m',
    'vermelho' : '\33[0;31m'}

print("--"*20)
print(f"{cores['magenta']}Vou pensar em um número entre 0 e 5. Tente adivinhar...{cores['limpa']}")
print("--"*20)

contador = 1
while contador != 0:
    num_jogador = int(input(f"Em que número pensei? {cores['amarelo']}"))
    num_computador = random.randint(0,5) #declara uma variável randomizada para o computador
    print(f"{cores['amarelo']}PROCESSANDO...{cores['limpa']}")
    sleep(2) #faz o computador esperar 2 segundos para o próximo passo

    if num_jogador == num_computador:
        print(f"{cores['verde']}PABABÉNS! Você conseguiu me vencer! {cores['limpa']}")
    else:
        print(f"{cores['vermelho']}PERDEU! Eu pensei no número {num_computador} e não no {num_jogador}!{cores['limpa']}")
    usuario = int(input("Deseja continuar jogando? Digite 1 para continuar e 0 para parar: "))
    contador = usuario
else:
    print(f"{cores['magenta']}Fim de jogo! Até a próxima!{cores['limpa']}")
