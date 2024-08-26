import os
os.system("cls || clear")

# Declarando variável.
peso_ideal = 0

# Solicitando dados.
altura = float(input("Digite sua altura: "))

sexo = input("Digite seu sexo (M ou F): ").upper() 

# Verfivicando.
match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
    case _:
        print("Opção inválida.")

print(f"Sexo: {sexo}")
print(f"Peso ideal: {peso_ideal:.2f}")
