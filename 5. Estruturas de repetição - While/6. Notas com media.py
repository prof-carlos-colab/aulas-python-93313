import os

os.system("cls || clear")

QUANTIDADE_NOTAS = 3 # Isto é uma constante.
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite {i+1} nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida! \nDigite novamente...")
        else: 
            # soma = soma + nota
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")
