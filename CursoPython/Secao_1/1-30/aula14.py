a = "A"
b = "B"
c = 1.1
string = "a={nome} b={nome2} c= {nome3:.2f}"
formato = string.format(nome=a, nome2=b, nome3=c)

print(formato)