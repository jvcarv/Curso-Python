"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = "amor"
letras_acertadas = ""
tentativas = 0

while True:
    letra = input("Digite uma letra: ")
    tentativas += 1


    if len(letra) > 1:
           print("Digite menos de uma letra.")
           continue
    
    if letra in palavra_secreta:
        letras_acertadas += letra


    palavra_acertada = ""
    for letra in palavra_secreta:
         if letra in letras_acertadas:
              palavra_acertada += letra
         else:
              palavra_acertada += "*"
    print(palavra_acertada)

    if palavra_acertada == palavra_secreta:
         print('Você ganhou!!!!!')
         print(f"A palavra secreta era {palavra_secreta}, e você a acertou em {tentativas} jogadas!")
         break



    

