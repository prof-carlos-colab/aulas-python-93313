import os

os.system("cls || clear")

contador = 0

while True:
    numero = int(input("Digite um número: "))

    if numero < 0:
        contador = contador + 1

    if numero == 0:
        break

print(f"Quantidade de número negativos: {contador}")