"""
Escrever um algoritmo que solicite ao usuário um número e 
faça a contagem regressiva até o número um aguardando um 
segundo para mostrar cada número.
"""

import os
import time
os.system("cls || clear")

numero = int(input("Digite um número: "))

for i in range(numero, 0, -1):
    print(i)
    time.sleep(1)

print("=== FIM ===")