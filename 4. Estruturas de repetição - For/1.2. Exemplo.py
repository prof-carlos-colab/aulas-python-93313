import os
import time

os.system("cls || clear")

print("Laço de repetição - For")
for i in range(1,6,2):
    print(f"Conteúdo da variável i = {i}")
    time.sleep(2) # Vai esperar 2 segundo.

print("=== FIM ===")