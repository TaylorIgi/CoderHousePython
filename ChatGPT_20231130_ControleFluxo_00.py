# Exercícios de Estruturas de Controle de Fluxo:

# 1. Escreva um programa que solicite ao usuário um número e determine se é par ou ímpar.
'''
def NumPar(MyNumber):
    if MyNumber % 2 == 0: return True
    else: return False

MyNumber = int(input("Digite o número que deseja analisar: "))
if NumPar(MyNumber): NumberType = "PAR"
else: NumberType = "ÍMPAR"
print(F"O número é {NumberType}")
'''

# 2. Crie um programa que simule um jogo de adivinhação, onde o usuário tenta adivinhar um número aleatório.

import random

# Gera um número inteiro aleatório entre 0 e 99
RandomNumber = random.randint(0, 99)

UserNumber = int(input("Digite seu palpite para o número (somente números inteiros entre 0 e 99): "))

if UserNumber == RandomNumber: print(f"Parabéns! Você acertou!!!")
else: print(f"Infelizmente você errou...\n O número correto era {RandomNumber}")