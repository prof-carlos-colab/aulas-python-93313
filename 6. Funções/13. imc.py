import os
os.system("cls || clear")

# Funções
def calcular_imc(peso, altura):
    resultado = peso / (altura * altura)
    return resultado

def verificar_classificacao(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc <= 24.9:
        return "Peso normal."
    elif imc <= 29.9:
        return "Sobrepeso."
    elif imc <= 34.9:
        return "Obesidade grau I."
    elif imc <= 39.9:
        return "Obesidade grau II."
    else: 
        return "Obesidade grau III."


# Entrada.
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# Processamento.
imc = calcular_imc(peso, altura)
classificacao = verificar_classificacao(imc)

# Saída.
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")