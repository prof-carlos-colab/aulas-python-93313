import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 4
lista_numeros = []
lista_negativos = []
lista_positivos = []

def verificar_numeros_negativos(lista_numeros):
    # Processamento.
    lista_de_negativos = []
    lista_de_positivos = []

    for numero in lista_numeros:
        if numero < 0:
            lista_de_negativos.append(numero) # Inserindo um número negativo na lista_de_negativos.
        else: 
            lista_de_positivos.append(numero) # Inserindo um número positivo na lista_de_positivos.
   
    # comando len() - retorna a quantidade de elementos no vetor/lista.
    quantidade_negativos = len(lista_de_negativos)

    # comando sum() - retorna a soma dos elementos no vetor/lista.
    soma_positivos = sum(lista_de_positivos)

    return quantidade_negativos, soma_positivos

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Processamento.
quantidade_de_negativos, soma_de_positivos = verificar_numeros(lista_numeros)

# Saída.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numeros):
    print(f"{contador+1}ª nota: {nota}")

print(f"\nQuantidade de negativos: {quantidade_de_negativos}")
print(f"Soma de positivos: {soma_de_positivos}")
