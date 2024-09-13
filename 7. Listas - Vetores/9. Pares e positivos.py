import os

os.system("cls || clear")

QUANTIDADE_NUMEROS = 3
lista_pares_positivos = []

# Entrada.
print("\n=== Solicintando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    while True:
        numero = int(input(f"Digite o {i+1}º número: "))

        # Verificando se o número é par e positivo.
        if numero % 2 == 0 and numero > 0:
            lista_pares_positivos.append(numero)
            break
        else: 
            print("Número inválido. \nTente novamente.\n\n")

# Saída.
print("\n=== Exibindo resultado ===")
for i, numero in enumerate(reversed(lista_pares_positivos)):
    print(f"{len(lista_pares_positivos)-i}º - {numero}")