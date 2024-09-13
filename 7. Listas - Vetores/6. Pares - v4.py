import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 4
lista_numeros = []
lista_negativos = []
lista_positivos = []

def verificar_numeros_negativos(lista_numeros):
    # Processamento.
    quantidade_negativos = 0

    for numero in lista_numeros:
        if numero < 0:
            quantidade_negativos += 1

    return quantidade_negativos

def verificar_numeros_positivos(lista_numeros):
    # Processamento.
    soma_positivos = 0
    
    for numero in lista_numeros:
        if numero > 0:
            soma_positivos += numero

    return soma_positivos


print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Processamento.
quantidade_de_negativos = verificar_numeros_negativos(lista_numeros)
soma_de_positivos = verificar_numeros_positivos(lista_numeros)

# Saída.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}ª nota: {nota}")

print(f"\nQuantidade de negativos: {quantidade_de_negativos}")
print(f"Soma de positivos: {soma_de_positivos}")
