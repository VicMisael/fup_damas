import pecas;
pecas.inicializar();
emJogo=True;
while(emJogo):
    jogadorInvalido=True;
    while(jogadorInvalido):
        print("Entre com o jogador")
        jogador=input().upper()
        if(jogador=="C" or jogador=="B"):
            jogadorInvalido=False;
        else:
           print("Jogador invalido!!!!")
    print("Entre com a jogada")
    jogada=input();
    pecas.fazerJogada(jogador,jogada)