import os

os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_de_numeros = []

print("=== Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))

    # Verificando se o número informado é negativo.
    if numero < 0:
        # Caso o número seja negativo, 
        # será substituido por zero.
        numero = 0

    # Inserindo número no vetor
    lista_de_numeros.append(numero)

print("\n=== Exibindo dados ===")
for cada_numero in lista_de_numeros:
    print(cada_numero)