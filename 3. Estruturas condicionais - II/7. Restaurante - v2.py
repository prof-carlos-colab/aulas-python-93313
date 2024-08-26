import os
os.system("cls || clear")

# Solicitando dados.
print("""
    1 - Picanha          R$ 25,00
    2 - Lasanha          R$ 20,00
    3 - Strogonoff       R$ 18,00
    4 - Bife Acebolado   R$ 15,00
    5 - Pão com ovo      R$ 5,00
      """)

opcao = int(input("Digite uma opção: "))

# Verificando
match opcao:
    case 1: 
        prato = "Picanha"
        preco = 25.00
    case 2: 
        prato = "Lasanha"
        preco = 20.00
    case 3: 
        prato = "Strogonoff"
        preco = 18.00
    case 4: 
        prato = "Bife Acebolado"
        preco = 15.00
    case 5: 
        prato = "Pão com ovo"
        preco = 5.00
    case _:
        print("(Opção inválida)")

print(f"Prato: {prato}")
print(f"Preço: R$ {preco}")
