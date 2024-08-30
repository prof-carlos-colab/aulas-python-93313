import os
os.system("cls || clear")

nota = float(input("Digite uma nota: "))

while nota < 0 or nota > 10:
    print("\nA nota deve ser maior ou igual a 0 e menor e igual a 10.")
    nota = float(input("Digite uma nota: "))

print(f"Nota: {nota}")
