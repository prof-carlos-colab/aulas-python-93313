import os
os.system("cls || clear")
   
# Solicitando dados.
numero = int(input("Digite um número para tabuada: "))
print(f"{numero} x {1} = {numero * 1}")
print(f"{numero} x {2} = {numero * 2}")
print(f"{numero} x {3} = {numero * 3}")
print(f"{numero} x {4} = {numero * 4}")
print(f"{numero} x {5} = {numero * 5}")
print(f"{numero} x {1} = {numero * 1}")
print(f"{numero} x {2} = {numero * 2}")
print(f"{numero} x {3} = {numero * 3}")
print(f"{numero} x {4} = {numero * 4}")
print(f"{numero} x {5} = {numero * 5}")


print(f"\nTabuada de multiplicação do número: {numero}")
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

