import pecas
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

    print("Entre com a jogada")
    jogada=input().upper()
    if(not jogadorInicialSetado):
        pecas.fazerJogada(jogador,jogada)
        pecas.proximoJogador()
        jogadorInicialSetado=True;
    else:
        pecas.fazerJogadaJogadorAutomatico(jogada)