import os

os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_de_numeros = []

def verificando_numeros(lista_de_numeros):
    lista_atualizada = []

    for numero in lista_de_numeros:
        # Verificando se o número informado é negativo.
        if numero < 0:
            # Caso o número seja negativo, 
            # será substituido por zero.
            numero = 0
        lista_atualizada.append(numero)
    
    return lista_atualizada

print("=== Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))

    # Inserindo número no vetor
    lista_de_numeros.append(numero)

lista_de_numeros = verificando_numeros(lista_de_numeros)

print("\n=== Exibindo dados ===")
for cada_numero in lista_de_numeros:
    print(cada_numero)
