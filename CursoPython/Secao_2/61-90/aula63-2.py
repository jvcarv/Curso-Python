"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 


def escopo():   
    global x #define que estou mexendo no X de fora da função, não criando uma para ela
    x = 10

    def outro_escopo():

        x = 11
        y = 2
        print(x,y)

    outro_escopo()
    print(x)

print(x)
escopo()
print(x)
