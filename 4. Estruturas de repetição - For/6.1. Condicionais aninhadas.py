import os
os.system("cls || clear")

nota = float(input("Digite uma nota: "))

if nota >= 7:
    print("Aprovado.")
else: 
    if nota < 4:
        print("Reprovado.")
    else: 
        print("Recuperação.")

print("=== FIM ===")    