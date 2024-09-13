import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 4
lista_notas = []

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Processamento.
soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else: 
    situacao = "Reprovado"

# Saída.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_notas):
    print(f"{contador+1}ª nota: {nota}")

print(f"Média: {media}")
print(f"Resultado: {situacao}")
