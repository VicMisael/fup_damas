import pecas
import render
import sys
pecas.inicializar()
emJogo=True
jogadorInvalido = True
jogadorInicialSetado=False;
jogador = ""
c=0
OFFLINE="O";
CONTRAJOGADOR="CJ";
v=sys.argv;
modoDeJogo=""
jogadas=None
if(len(v)>1):
    txt=v[1]
    file=txt.split(".")
    try:
        if(file[1]=="txt"):
           dados=open(txt,"r",encoding="utf-8")
           jogadas=dados.read()
           modoDeJogo=OFFLINE
           jogadas=jogadas.split("\n")               
    except:
        print("Invalido, inicando no modo CJ")
        modoDeJogo=CONTRAJOGADOR
    

else:
    modoDeJogo="CJ"

if(modoDeJogo==OFFLINE):
    i=0
    while(i<len(jogadas) and emJogo):

        if(jogadorInvalido):
            jogador = jogadas[0]
            if(not(jogador=="C" or jogador=="B")):
                jogadorInvalido=False
                emJogo=False
                render.mostrarErro("Primeira linha invalida")
        if(i!=0):
            jogada=jogadas[i]
            render.limpar()
            if(pecas.fazerJogada(jogador,jogada)):
                if(jogador=="C"):
                    jogador="B"
                if(jogador=="B"):
                    jogador="C"
            if(pecas.retornarValidezDaJogada()):
                render.showJogadaInvalida("Jogada invalida na linha"+str(i+1))
        i+=1
if(modoDeJogo==CONTRAJOGADOR):
    while(emJogo):

        while(jogadorInvalido):
            print("Entre com o jogador")
            jogador = input().upper()
            if(jogador=="C" or jogador=="B"):
                jogadorInvalido=False
            else:
                render.showJogadaInvalida("");
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
            elif(jogador=="B"):
                jogador="C"
        if(pecas.getFimDoJogo()):
            print("Deseja continuar jogando")
            opcao=""
            while(not(opcao=="S" or opcao=="N")):
                opcao=input().upper
            if(opcao=="S"):
                pecas.reiniciar
            if(opcao=="N"):
                emJogo=False


        
    