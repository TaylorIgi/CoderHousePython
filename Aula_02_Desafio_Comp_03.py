# Faça um programa que peça ao usuário para digitar uma lista de nomes separados por virgula.
# Transforme essa lista em uma lista de strings.

lista_nomes = input("Digite uma lista com nomes separados por virgula:\n")
lista_string = lista_nomes.split(',')
cont = 1
cont_nomes = lista_nomes.count(',') + 1

while cont <= cont_nomes:
    lista_string[cont - 1] = lista_string[cont - 1].strip().capitalize()
    cont = cont + 1

print("A lista de nomes alocados em uma lista de strings é:")
print(lista_string)