while True:
    num_1 = input("Digite o primeiro número: ")
    num_2 = input("Digite o segundo  número: ")
    operador = input("Digite o operador desejado (+-/*): ")
    resultado = ...
    
    numeros_validos = None
    num_1_int = 0
    num_2_int = 0

    try:

        num_1_int = float(num_1)
        num_2_int = float(num_2)
        numeros_validos = True
        
    except:
        numeros_validos = None

        if numeros_validos == None:
            print("Digite um ou ambos números válidos.")
            continue

    operadores_validos = "*/+-"

    if operador not in operadores_validos:
        print("Digite um operador válido.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador válido.")
        continue

    if operador == "+":
            resultado = f'{num_1_int} + {num_2_int} = {num_1_int+num_2_int}' 
    elif operador == "-":
            resultado = f'{num_1_int} - {num_2_int} = {num_1_int-num_2_int}'  
    elif operador == "/":
            resultado = f'{num_1_int} / {num_2_int} = {num_1_int/num_2_int}' 
    elif operador == "*":
            resultado = f'{num_1_int} * {num_2_int} = {num_1_int*num_2_int}' 
    
        
    print(f'O resultado da sua conta é igual a: {resultado}')
        
    sair = input("Digite [S] para Sair do sistema, qualquer outra coisa para continuar: ").lower().startswith("s")

    if sair is True:
        break    