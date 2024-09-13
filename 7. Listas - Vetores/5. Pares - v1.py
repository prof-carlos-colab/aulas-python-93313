import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 6
lista_numeros = []
pares = 0
impares = 0

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

    # Processamento.
    if numero % 2 == 0:
        pares += 1
    else: 
        impares += 1

# Saída.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}ª nota: {nota}")

print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
