import os
os.system("cls || clear")

# Solicitando dados.
dia = int(input("Digite um número para o dia da semana: "))

# Verificando.
match dia: 
    case 1: 
        print("Fim de semana.")
    case 2: 
        print("Dia útil.")
    case 3: 
        print("Dia útil.")
    case 4: 
        print("Dia útil.")
    case 5: 
        print("Dia útil.")
    case 6: 
        print("Dia útil.")
    case 7: 
        print("Fim de semana.")
    case _: 
        print("Opção inválida.")