import os
os.system("cls || clear")

# Solicitando dados.
primeira_numero = float(input("Digite o primeiro numero: "))
segunda_numero = float(input("Digite o segundo numero: "))

# Verificando.
soma = primeira_numero + segunda_numero
produto = primeira_numero * segunda_numero
media = soma / 2

if (primeira_numero > segunda_numero):
    maior = primeira_numero
    menor = segunda_numero
else: 
    maior = segunda_numero
    menor = primeira_numero

# Exibindo dados.
print("\nExibindo resultados: ")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")


