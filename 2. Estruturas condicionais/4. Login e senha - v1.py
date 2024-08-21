import os
os.system("cls || clear")

# Solicitando dados.
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Verificar.
if login == "marta" and senha == "123":
    print("Bem-vindo!")
else: 
    print("Login ou senha inválidos.")