#programa para um jogo simples: adivinha o numero
"""
_author_: André Lascas
_version_:1.0.0
_source_: VASCONCELOS, José Braga de; RIBEIRO, Nuno - Título: Tecnologias de Programação de Jogos,
FCA Editora
"""

import random

tentativa = 0
adivinha = 0
nome = input("Qual o teu nome jogador? ")
num = random.randint(1,20)
print(nome+ ', adivinha o número que estou a pensar entre 1 e 20')

#loop para jogar
while (tentativa < 5) and (adivinha != num):
    adivinha = input('Adivinha: ')
    adivinha = int(adivinha)
    tentativa = tentativa + 1

    if adivinha < num:
        print('Numero pequeno')
    if adivinha > num:
        print('Numero grande')

if adivinha == num:
    tentativa = str(tentativa) #cast de numero para string
    print (nome+ ', adivinhaste o numero em '+tentativa+' tentativas!')
else:
    num = str(num)
    print('O número que estava a pensar era o '+num)
