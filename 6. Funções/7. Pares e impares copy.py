"""
Crie uma função que receba um número e mostre uma mensagem informando 
se o número é par ou ímpar.   
"""

import os

os.system("cls || clear")

# Processamento.
def verificar_numero(numero):
    if numero % 2 == 0:
        print("Par.")
    else: 
        print("Impar.")

# Entrada de dados.
print("=== Solicitando dados ===")
numero = int(input("Digite um número: "))

# Saída.
verificar_numero(numero)