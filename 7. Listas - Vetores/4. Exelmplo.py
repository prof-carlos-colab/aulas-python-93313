import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 5
lista_numeros = []

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Processamento.
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

# Saída.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}ª nota: {nota}")

print(f"\nMenor número: {menor_numero}")
print(f"Maior número: {maior_numero}")
