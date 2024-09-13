"""
Escreva um programa que solicite ao usuário o ano de nascimento e, 
utilizando uma função, retorne com a idade do usuário.
"""
import os

os.system("cls || clear")

def calcular_idade_ano_nascimento(ano_nascimento):
    return 2024 - ano_nascimento

# Entrada.
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# Processamento.
idade = calcular_idade_ano_nascimento(ano_nascimento)

# Saída.
print("=== RESULTADO ===")
print(f"Idade: {idade}")