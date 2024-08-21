import os
os.system("cls || clear")

# Solicitar dados.
idade = int(input("Digite sua idade: "))

# Verificar.
if idade >= 18 and idade <= 65:
    print("Voto obrigatório.")
else: 
    print("Não é obrigado a votar.")