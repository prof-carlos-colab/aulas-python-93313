import os
os.system("cls || clear")

# Solicitando dados.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

# Verificando.
soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3

if media >= 7:
    resultado = "Aprovado."
else: 
    resultado = "Reprovado."

# Exibindo dados.
print("\nExibindo resultados: ")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Média: {media}")
print(f"Resultado: {resultado}")


