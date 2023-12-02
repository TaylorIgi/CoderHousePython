# Faça um programa que crie uma lista vaza e permita que o usuário insira 5 números inteiros na lista.

lista_inteiros = [None]*5
cont_inteiros = 1

while cont_inteiros <= 5:
    check_inteiro = str(input(f"Digite o {cont_inteiros}o número inteiro:"))
    check_inteiro = float(check_inteiro.replace(",", "."))
    if round(check_inteiro,0) == check_inteiro:
        lista_inteiros[cont_inteiros-1] = int(check_inteiro)
        cont_inteiros = cont_inteiros + 1
    else:
        print("O número informado não é inteiro")

print(f"A lista de inteiros é: {lista_inteiros}")