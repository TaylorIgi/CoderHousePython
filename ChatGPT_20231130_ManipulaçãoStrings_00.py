# Exercícios de manipulação de Strings:

# 1. Crie uma função que receba uma string e retorne a mesma string invertida.

def InverteString(MyString):
    StringInvertida = ""
    for contador in range(0,len(MyString)):
        StringInvertida = StringInvertida + MyString[-(contador+1)]
        contador += 1
    return StringInvertida

'''
StringTeste = input("Digite a string que gostaria de inverter:\n")
print(f"A string invertida é: \n{InverteString(StringTeste)}")
'''

# 2. Escreva um programa que conte o número de vogais em uma palavra.
'''
def ContaVogais(MyString):
    contador = 0
    for letra in range(0, len(MyString)):
        if MyString[letra].capitalize() in ["A", "E", "I", "O", "U"]:
            contador += 1
    return contador

StringTeste = input("Digite a string:\n")
print(f"A quantidade de vogais é: {ContaVogais(StringTeste)}")
'''
# 3. Implemente uma função que verifique se uma palavra é um palíndromo.

def CheckPalindromo(MyString):
    if MyString.capitalize() == InverteString(MyString).capitalize():
        return True
    else:
        return False

PalavraTeste = input("Digite a palavra:")
if CheckPalindromo(PalavraTeste):
    print(f"A palavra {PalavraTeste} é um palíndromo")
else:
    print(f"A palavra {PalavraTeste} NÃO é um palíndromo")