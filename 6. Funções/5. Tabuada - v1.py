"""
Faça um programa que imprime a tabuada de um número informado pelo usuário 
de 1 a 10 utilizando uma função para exibir o resultado.
"""

import os

os.system("cls || clear")

# Processamento
def mostrar_tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

# Entrada de dados.
numero = int(input("Digite um número: "))

# Saída
mostrar_tabuada(numero)