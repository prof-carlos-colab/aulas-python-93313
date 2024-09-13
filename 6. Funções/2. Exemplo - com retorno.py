import os

os.system("cls || clear")

# Função com retorno.
def somar(primeiro_numero, segundo_numero):
    soma = primeiro_numero + segundo_numero
    return soma


primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

soma = somar(primeiro_numero, segundo_numero)

print(f"Soma: {soma}")
