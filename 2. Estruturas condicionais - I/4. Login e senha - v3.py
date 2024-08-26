import os
os.system("cls || clear")

# Solicitando dados.
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Verificar.
login_correto = login == "marta" # True
senha_correto = senha == "123" # False

if login_correto and senha_correto:
    print("Bem-vindo!")
else: 
    print("Login ou senha inválidos.")