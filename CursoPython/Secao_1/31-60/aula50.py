lista = []

while True:
    controle = input(f"Selecione uma opção \n[i]nserir  [a]pagar  [l]istar \n").lower()
    
    if controle == "i":
        valor = input("Valor: ")
        lista.append(valor)
    elif controle == 'a':
        try:
            indice = input("Escolha o índice que deseja apagar: ")
            del lista[indice]
        except ValueError:
            print("Informe um número inteiro.")
        except IndexError:
            print("Informe um índice válido")
        except Exception:
            print("Informe um índice válido")
    elif controle == "l":

        if len(lista) == 0:
            print("Nada para lista.")

        for indice, item in enumerate(lista):
            print(indice, item)
    else:
        print("Digite uma opção válida.")

