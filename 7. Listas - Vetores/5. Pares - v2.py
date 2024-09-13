import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 6
lista_numeros = []
pares = 0
impares = 0

def verificar_pares_impares(numeros):
    qtd_pares = 0
    qtd_impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            qtd_pares += 1
        else: 
            qtd_impares += 1
    return qtd_pares, qtd_impares   

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Processamento.
pares, impares = verificar_pares_impares(lista_numeros)

# Saída.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}ª nota: {nota}")

print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
