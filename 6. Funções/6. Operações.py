"""
Crie funções que recebam 2 números e retorne a 
soma, subtração, divisão e a multiplicação destes 
dois números informados.

Obs.: Crie uma função para cada operação.
"""

import os

os.system("cls || clear")

# Funções:
def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def dividir(primeiro_numero, segundo_numero):
    return primeiro_numero / segundo_numero


# Solicitando dados (Entrada).
print("\n === Solicitando dados ===")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# Processamento.
soma = somar(primeiro_numero, segundo_numero)
subtracao = subtrair(primeiro_numero, segundo_numero)
multiplicacao = multiplicar(primeiro_numero, segundo_numero)
divisao = dividir(primeiro_numero, segundo_numero)

# Exibindo dados (Saída).
print("\n === Exibindo resultados ===")
print(f"Soma: {soma}")
print(f"subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
