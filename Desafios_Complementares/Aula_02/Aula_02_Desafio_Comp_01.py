# Escreva um programa em Python que calcule o IMC e uma pessoa.
# O programa deve solicitar ao usuário o peso em kg e a altura em metros, e em seguida calcular e imprimir o IMC

peso = str(input("Digite o peso em kg: "))
altura = str(input("Digite a altura em metros: "))

peso_aj = peso.replace(",",".")
altura_aj = altura.replace(",", ".")

peso_aj = float(peso_aj)
altura_aj = float(altura_aj)

imc = peso_aj/(altura_aj**2)

print(f"O IMC de uma pessoa com {round(peso_aj,2)}kg e {round(altura_aj,2)}m é {round(imc,2)}")