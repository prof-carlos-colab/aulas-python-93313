"""
Escreva um programa que permita ler 2 notas de um aluno e: 
- Informe por meio de uma função a média;
- Informe por meio de uma função se a média for maior ou igual a 7, 
o aluno estará aprovado, caso contrário, estará reprovado.
"""
import os

os.system("cls || clear")

def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma / 2
    return media

def verificar_resultado(media):
    if media >= 7:
        return "Aprovado"
    else: 
        return "Reprovado"

# Entrada.  
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

# Processamento.
media = calcular_media(primeira_nota, segunda_nota)
resultado = verificar_resultado(media)

# Saída.
print("=== Resultado ===")
print(f"Média: {media}")
print(f"Resultado: {resultado}")