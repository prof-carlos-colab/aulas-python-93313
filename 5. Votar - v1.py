import os
os.system("cls || clear")

# Solicitar dados.
idade = int(input("Digite sua idade: "))

# Verificar.
if idade < 18 or idade > 65:
    print("Não é obrigado a votar.")
else: 
    print("Voto obrigatório.")