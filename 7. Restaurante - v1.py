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
        print("Prato: Picanha")
        print("Preço: R$ 25,00")
    case 2: 
        print("Prato: Lasanha")
        print("Preço: R$ 20,00")
    case 3: 
        print("Prato: Strogonoff")
        print("Preço: R$ 18,00")
    case 4: 
        print("Prato: Bife Acebolado")
        print("Preço: R$ 15,00")
    case 5: 
        print("Prato: Pão do ovo")
        print("Preço: R$ 5,00")
    case _:
        print("(Opção inválida)")

