import os
os.system("cls || clear")

# Solicitando dados.
dia = int(input("Digite um número para o dia da semana: "))

# Verificando.
match dia: 
    case 1 | 7: 
        print("Fim de semana.")
    case 2 | 3 | 4 | 5 | 6 : 
        print("Dia útil.")
    case _: 
        print("Opção inválida.")