import os
os.system("cls || clear")

nota = float(input("Digite uma nota: "))

if nota >= 7:
    print("Aprovado.")
elif nota < 4: # else if 
    print("Reprovado.")
else: 
    print("Recuperação.")

print("=== FIM ===")    