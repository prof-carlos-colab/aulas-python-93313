"""
Fazer um programa que solicita o preço de um produto e inflaciona esse preço em 10% se ele 
for menor que 100 e em 20% se ele for maior ou igual a 100. 

Utilize uma função para obter o resultado solicitado.
"""
import os

os.system("cls || clear")

def inflacionar(preco_produto):
    if preco_produto <= 100:
        # return (preco_produto * 0.1) + preco_produto
        return preco_produto * 1.1
    else: 
        return preco_produto * 1.2

# Entrada.
preco_produto = float(input("Digite o preço de um produto: "))

# Processamento.
preco_inflacionado = inflacionar(preco_produto)

# Saída.
print("\n=== RESULTADO ===")
print(f"Preço inflacionado: {preco_inflacionado:.2f}")