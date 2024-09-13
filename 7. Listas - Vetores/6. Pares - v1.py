import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 4
lista_numeros = []
lista_negativos = []
lista_positivos = []

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

    # Processamento.
    if numero < 0:
        lista_negativos.append(numero) # Inserindo um número negativo na lista_negativos.
    else: 
        lista_positivos.append(numero) # Inserindo um número positivo na lista_positivos.

# comando len() - retorna a quantidade de elementos no vetor/lista.
quantidade_negativos = len(lista_negativos)

# comando sum() - retorna a soma dos elementos no vetor/lista.
soma_positivos = sum(lista_positivos)

# Saída.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}ª nota: {nota}")

print(f"\nQuantidade de negativos: {quantidade_negativos}")
print(f"Soma de positivos: {soma_positivos}")
