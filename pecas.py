import render
import math
posicoes=[" "]*100
pecasPadrao=["o","@"]
pecasDama=["O","&"]
scores=[0,0]


#Vai inicializar o tabuleiro e colocar as peças nas suas posições padrões
def inicializar():
        global posicoes
        for i in range(100):
                if((i//10)%2==0):
                        if(i%2==0):
                                posicoes[i]="#"
                else:
                        if(i%2==1):
                                posicoes[i]="#"
        for a in range(30):
                if(posicoes[a]!="#"):
                        posicoes[a]=pecasPadrao[0]
        a=0
        for a in range(60,100):
                if(posicoes[a]!="#"):
                        posicoes[a]=pecasPadrao[1]
        render.renderizar(posicoes)

def fazerJogada(jogador,jogada):
        render.limpar()
        vetJog=jogada.split("--")
        endInicial=pegarEnderecoDaTabela(vetJog[0])
        endFinal=pegarEnderecoDaTabela(vetJog[1])
        proximoJogador=False;
        if endInicial[0]==-1 or endInicial[1]==-1  or endFinal[0]==-1 or endFinal[1]==-1:
                render.showJogadaInvalida("")
                return
        (x1,y1)=endInicial
        (x2,y2)=endFinal
        distancia = getDistancia(x1, y1, x2, y2)

        if getPecaAtPosicao(x1,y1)=="#" or getPecaAtPosicao(x2,y2)=="#" or getPecaAtPosicao(x1,y1)==" " :
                render.showJogadaInvalida("")

        elif(distancia==-1):
                render.showJogadaInvalida("")
        else:

                if(distancia==1):
                        if jogador=="B" and (getPecaAtPosicao(x1,y1)=="@" or getPecaAtPosicao(x1,y1)=="&"):
                                if(checarPecasAoRedor(x1,y1,jogador)):
                                        moverPeca(x1,y1,x2,y2)
                                        proximoJogador=True;
                        elif jogador=="C" and (getPecaAtPosicao(x1,y1)=="o" or getPecaAtPosicao(x1,y1)=="O"):
                                if(checarPecasAoRedor(x1,y1,jogador)):
                                        moverPeca(x1,y1,x2,y2)
                                        proximoJogador=True;

                if(distancia==2):
                        #Como pra comer uma peça a distancia tem de ser 2,vai checar a peça do meio e comer e contar o placar
                        if jogador=="B" and (getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="o") or getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="O"  :
                                comerPeca(jogador,"N",(x1+x2)//2,(y1+y2)//2)
                                moverPeca(x1, y1, x2, y2)
                        elif jogador=="C" and (getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="@" or getPecaAtPosicao((x1+x2)/2,(y1+y2)//2)=="&"):
                                comerPeca(jogador, "N", (x1+x2) // 2, (y1+y2) // 2)
                                moverPeca( x1, y1, x2, y2)
                        else:
                                render.showJogadaInvalida("")
                if(distancia>2):
                        if(getPecaAtPosicao(x1,y1)=="&") or (getPecaAtPosicao(x1,y1)=="O"):
                                if(checarPecasEComerComDamas(x1,y1,x2,y2,jogador)):
                                        moverPeca(x1,y1,x2,y2)
                                else:
                                        render.showJogadaInvalida("")
                        else:
                                render.showJogadaInvalida("")

                #vai checar se alguma peça pode se tornar dama
                for i in range(10):
                        if(getPecaAtPosicao(i,9)=="o"):
                                setPecaAtPosicao("&",i,0)
                for i in range(10):
                        if(getPecaAtPosicao(i,0)=="@"):
                                setPecaAtPosicao("&",i,0)
       
        print()
        render.renderizar(posicoes)
        print("Jogado de Baixo:",scores[0],"Pontos \nJogador de cima:",scores[1],"Pontos")
        return proximoJogador
#Essas de baixo aq tão obviasB
def checarPecasEComerComDamas(x1,y1,x2,y2,jogador):
        subX=False
        subY=False
        if(x1>x2):
                subX=True
        if(y1>y2):
                subY=True
        xAux=x1
        yAux=y1
        npecascomiveis=0
        jogadaProibida=False
        pecaPosX=None
        pecaPosY=None
        while(not(x2==xAux and yAux==y2) and not jogadaProibida):
                if(subX):
                        xAux-=1
                else:
                        xAux+=1
                if(subY):
                        yAux-=1
                else:
                        yAux+=1
                if(getPecaAtPosicao(xAux,yAux)=="@" or getPecaAtPosicao(xAux,yAux)=="&"):
                        if(jogador=="C"):
                                npecascomiveis+=1;
                                if(pecaPosX==None and pecaPosY==None):
                                        pecaPosX=xAux
                                        pecaPosY=yAux
                if(getPecaAtPosicao(xAux,yAux)=="o" or getPecaAtPosicao(xAux,yAux)=="O"):
                        if(jogador=="B"):
                                npecascomiveis+=1;
                                if(pecaPosX==None and pecaPosY==None):
                                        pecaPosX=xAux
                                        pecaPosY=yAux
                                
        
        
        
        if(npecascomiveis>1):
               
                jogadaProibida=True
        else:
                comerPeca(jogador,"N",pecaPosX,pecaPosY)  
                
        return not jogadaProibida
                              
def checarPecasAoRedor(xIni,yIni,jogador):
        #print("A ser implementada")       
        deveComer=False;
        xInipos=0;
        yInipos=0;
        if(jogador=="B"):
                if(getPecaAtPosicao((xIni+1),(yIni+1))=="o" or getPecaAtPosicao((xIni+1),(yIni+1))=="O" ):
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni+1
   
                if(getPecaAtPosicao(xIni+1,yIni-1)=="o" or getPecaAtPosicao(xIni+1,yIni-1)=="O" ):
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni-1
            
                if(getPecaAtPosicao(xIni-1,yIni+1)=="o" or getPecaAtPosicao(xIni-1,yIni+1)=="O" ):
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni+1
                
                if(getPecaAtPosicao(xIni-1,yIni-1)=="o" or getPecaAtPosicao(xIni-1,yIni-1)=="O" ):
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni-1
        if(jogador=="C"):
                if(getPecaAtPosicao(xIni+1,yIni+1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" ):
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni+1
                if(getPecaAtPosicao(xIni+1,yIni-1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" ):
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni-1
                if(getPecaAtPosicao(xIni-1,yIni+1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" ):
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni+1
                if(getPecaAtPosicao(xIni-1,yIni-1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" ):
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni-1
        if(deveComer):
                render.showJogadaInvalida("Você Deve comer a peça na posição "+pegarLetraTabela(xInipos)+","+str(yInipos))
        return not deveComer
def setPecaAtPosicao(peca,x,y):
        global posicoes
        posicoes[x+y*10]=peca
def getPecaAtPosicao(x,y):
        return posicoes[x+y*10]

def comerPeca(jogador,modo,x,y):
       if(modo=="N"):
               setPecaAtPosicao(" ", x, y)
               if jogador == "B":
                       scores[0] += 1;
               if jogador == "C":
                       scores[1]+=1;




def getTipoPeca(peca):
        if(peca=="o" or peca=="@"):
                return "N"
        elif(peca=="O" or peca=="&"):
                return "D"
        else:
                return"E"
def moverPeca(x1,y1,x2,y2):
        pecaPosIni=getPecaAtPosicao(x1,y1)
        if(pecaPosIni=="&" or pecaPosIni=="@" or pecaPosIni=="o" or pecaPosIni=="O" ):
                setPecaAtPosicao(pecaPosIni, x2, y2)
                setPecaAtPosicao(" ", x1, y1)
        else:
                render.showJogadaInvalida("")

def getDistancia(x1,y1,x2,y2):
        #vai pegar a distancia percorrida pela peça
      distX=math.fabs(x2-x1)
      distY=math.fabs(y2-y1)
      if distX==distY:
        return distX
      else:
        return -1;  
        

def pegarLetraTabela(num):
        if num==0:
                return "A"
        elif num==1:
                return "B"
        elif num==2:
                return "C"
        elif num==3:
                return "D"
        elif num==4:
                return "E"
        elif num==5:
                return "F"
        elif num==6:
                return "G"
        elif num==7:
                return "H"
        elif num==8:
                return "I"
        elif num==9:
                return "J"
        else:
                return"Erro"


def pegarEnderecoDaTabela(endereco):
        #Vai traduzir o endereço da coluna para numeros,para tornar o acesso ao vetor de peças mais fácil
        endY=int(endereco[1])
        endX=-1
        letra=endereco[0]
        letra=letra.upper()
        if letra=="A":
                endX=0
        elif letra=="B":
                endX=1
        elif letra=="C":
                endX=2
        elif letra=="D":
                endX=3
        elif letra=="E":
                endX=4
        elif letra=="F":
                endX=5
        elif letra=="G":
                endX=6
        elif letra=="H":
                endX=7
        elif letra=="I":
                endX=8
        elif letra=="J":
                endX=9
        if(endY>9):
                endY=-1
        end=[endX,endY]  
        return end
#Código pra teste
inicializar()
v=[]
v.append(fazerJogada("B","B6--C5"))
v.append(fazerJogada("C","D2--C3"))
v.append(fazerJogada("C","C3--D4"))
v.append(fazerJogada("B","C5--E3"))
v.append(fazerJogada("B","E3--D2"))
v.append(fazerJogada("C","F2--G3"))
v.append(fazerJogada("C","G3--H4"))
v.append(fazerJogada("C","E1--F2"))
v.append(fazerJogada("C","F0--E1"))
v.append(fazerJogada("B","D2--F0"))
v.append(fazerJogada("C","C1--D2"))
v.append(fazerJogada("C","B2--C3"))
v.append(fazerJogada("C","C3--B4"))
v.append(fazerJogada("B","F0--A5"))
v.append(fazerJogada("B","H6--G5"))
v.append(fazerJogada("B","G5--F4"))
print(v)