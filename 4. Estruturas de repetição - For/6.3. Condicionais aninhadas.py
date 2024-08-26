import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 2 # Uma constante
soma = 0

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    soma = soma + nota

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    print("Aprovado.")
elif media >= 5: # else if 
    print("Recuperação.")
elif media >= 4: # else if 
    print("Conselho de classe.")
else: 
    print("Reprovado.")

print("=== FIM ===")    