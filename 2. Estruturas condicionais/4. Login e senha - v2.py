import os
os.system("cls || clear")

# Declarando variáveis.
login_salvo = "marta"
senha_salva = "123"

# Solicitando dados.
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Verificar.
if login == login_salvo and senha == senha_salva:
    print("Bem-vindo!")
else: 
    print("Login ou senha inválidos.")