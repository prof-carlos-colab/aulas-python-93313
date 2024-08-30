"""
Crie um programa que solicite ao usuário seu 
login e uma senha. 

O programa deve continuar pedindo o login e a senha 
até que ambos estejam corretos. 

Com apenas 3 tentativas.
"""

import os
os.system("cls || clear")

login_salvo = "Marta"
senha_salva = "123"

for i in range(3):
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login_salvo == login and senha_salva == senha:
        print("Bem-vindo!")
        break
    else:
        print("Login ou senha inválidos.")

print("=== FIM ===")
   