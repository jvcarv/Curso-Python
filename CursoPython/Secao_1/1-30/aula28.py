numero_str = input("Digite um número, e lhe mostrarei o dobro: ")

try:
  numero_float = float(numero_str)
  print(f"O dobro do número digitado ({numero_float}) é igual a {numero_float*2}")
except:
  print("Você não digitou um número")