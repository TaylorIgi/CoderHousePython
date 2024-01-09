# Exercícios de listas

# 1. Crie uma lista de números e escreva um programa que encontre o maior e o menor número na lista.
'''
def FindMax(MyList):
    MyMax = MyList[0]
    for Num in MyList:
        if Num > MyMax: MyMax = Num
        i =+ 1
    return MyMax

def FindMin(MyList):
    MyMin = MyList[0]
    for Num in MyList:
        if Num < MyMin: MyMin = Num
        i =+ 1
    return MyMin

import random
TestList = []
for i in range(0,10):
    TestList.append(random.randint(0,99))

MaxNum = FindMax(TestList)
MinNum = FindMin(TestList)
print(f"A lista é: {TestList}")
print(f"O maior número é: {MaxNum}")
print(f"O menor número é: {MinNum}")
'''

# 2. Implemente uma função que remova elementos duplicados de uma lista.
def RemoveDuplicates(MyList):
    CleanList = []
    CleanList.append(MyList[0])
    for i in range(1,len(MyList)):
        if MyList[i] not in CleanList: CleanList.append(MyList[i])
        i =+ 1
    return CleanList

import random
TestList = []
for i in range(0,10):
    TestList.append(random.randint(0,9))

print(f"Lista original: {TestList}")
print(f"Lista ajustada: {RemoveDuplicates(TestList)}")