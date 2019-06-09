import pecas
import render
pecas.inicializar()
emJogo=True
jogadorInvalido = True
jogadorInicialSetado=False;
jogador = ""
c=0
while(emJogo):

    while(jogadorInvalido):
        print("Entre com o jogador")
        jogador = input().upper()
        if(jogador=="C" or jogador=="B"):
            jogadorInvalido=False
        else:
            print("Jogador invalido!!")
    print(jogador)
    if (jogador == "C"):
        print("o jogador de cima é o proximo")
    if (jogador == "B"):
        print("o jogador de baixo é o proximo")

    print("Entre com a jogada")
    jogada=input().upper()
    render.limpar()
    if(pecas.fazerJogada(jogador,jogada)):
        if(jogador=="C"):
            jogador="B"
        if(jogador=="B"):
            jogador="C"
    