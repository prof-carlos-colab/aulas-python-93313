import os
os.system("cls || clear")

resultado = 0

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
opcao = input("Digite uma opção (+ - * /): ")

match(opcao): 
    case "+": 
        resultado = primeiro_numero + segundo_numero
    case "-": 
        resultado = primeiro_numero - segundo_numero
    case "*": 
        resultado = primeiro_numero * segundo_numero
    case "/": 
        resultado = primeiro_numero / segundo_numero
    case _: 
        print("Opção inválida.")

print(f"Resultado: {resultado}")
print("=== FIM ===")
