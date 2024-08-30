contador = 0
continua = 's'

while continua == 's':
    # comandos a serem repetidos
    print("Repentindo....")
    
    contador += 1
    # contador = contador + 1
    
    continua = input("Tecle 's' se deseja continuar: ").strip().lower()

if contador == 0:
    print("O bloco NAO foi repetido.")
else:
    print(f"O bloco foi repetido {contador} vezes")
