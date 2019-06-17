import render
import math
fimDoJogo=False
posicoes=[" "]*100
pecasPadrao=["o","@"]
pecasDama=["O","&"]
scores=[0,0]
jogadaInvalida=False;

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
def reiniciar():
        posicoes=[" "]*100;
        scores=[0,0]
        inicializar();

def fazerJogada(jogador,jogada):
        
        render.limpar()
        vetJog=jogada.split("--")
        endInicial=pegarEnderecoDaTabela(vetJog[0])
        endFinal=pegarEnderecoDaTabela(vetJog[1])
        proximoJogador=False;
        if endInicial[0]==-1 or endInicial[1]==-1  or endFinal[0]==-1 or endFinal[1]==-1:
                showJogadaInvalida("")
                return
        (x1,y1)=endInicial
        (x2,y2)=endFinal
        distancia = getDistancia(x1, y1, x2, y2)

        if getPecaAtPosicao(x1,y1)=="#" or getPecaAtPosicao(x2,y2)=="#" or getPecaAtPosicao(x1,y1)==" " :
                showJogadaInvalida("")

        elif(distancia==-1):
                showJogadaInvalida("")
        else:

                if(distancia==1):
                        if jogador=="B" and (getPecaAtPosicao(x1,y1)=="@" or getPecaAtPosicao(x1,y1)=="&"):
                                if(checarPecasAoRedor(x1,y1,jogador) ):
                                        if(y1>y2):
                                                moverPeca(x1,y1,x2,y2)
                                                proximoJogador=True;
                                        else:
                                                showJogadaInvalida("Você só pode voltar se for comendo")
                        elif jogador=="C" and (getPecaAtPosicao(x1,y1)=="o" or getPecaAtPosicao(x1,y1)=="O"):
                                if(checarPecasAoRedor(x1,y1,jogador)):
                                        if(y1<y2):
                                                moverPeca(x1,y1,x2,y2)
                                                proximoJogador=True;
                                        else:
                                                showJogadaInvalida("Você só voltar se for comendo")
                                
                if(distancia==2):
                        #Como pra comer uma peça a distancia tem de ser 2,vai checar a peça do meio e comer e contar o placar
                        if jogador=="B" and (getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="o") or getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="O"  :
                                comerPeca(jogador,"N",(x1+x2)//2,(y1+y2)//2)
                                moverPeca(x1, y1, x2, y2)
                        elif jogador=="C" and (getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="@" or getPecaAtPosicao((x1+x2)/2,(y1+y2)//2)=="&"):
                                comerPeca(jogador, "N", (x1+x2) // 2, (y1+y2) // 2)
                                moverPeca( x1, y1, x2, y2)
                        else:
                                showJogadaInvalida("")
                if(distancia>2):
                        if(getPecaAtPosicao(x1,y1)=="&") or (getPecaAtPosicao(x1,y1)=="O"):
                                if(checarPecasEComerComDamas(x1,y1,x2,y2,jogador)):
                                        moverPeca(x1,y1,x2,y2)
                                else:
                                        showJogadaInvalida("")
                        else:
                                showJogadaInvalida("")

                #vai checar se alguma peça pode se tornar dama
                for i in range(10):
                        if(getPecaAtPosicao(i,9)=="o"):
                                setPecaAtPosicao("&",i,0)
                for i in range(10):
                        if(getPecaAtPosicao(i,0)=="@"):
                                setPecaAtPosicao("&",i,0)
       
        render.renderizar(posicoes)
        global fimDoJogo;
        
        if(contarPecasJogadorDeCima()==0):
                fimDoJogo=True;
                render.venceu("O jogador de baixo venceu")
        if(contarPecasJogadorDeBaixo()==0):
                fimDoJogo=True;
                render.venceu("O jogador de cima venceu")
        
        #print("Jogador de Baixo:",scores[0],"Pontos \nJogador de cima:",scores[1],"Pontos")
        return proximoJogador
#Essas de baixo aq tão obviasB
def retornarValidezDaJogada():
        global jogadaInvalida
        aux=jogadaInvalida
        if(aux):
                jogadaInvalida=False;
        return aux
def showJogadaInvalida(mAdc):
        global jogadaInvalida
        jogadaInvalida=True;
        render.showJogadaInvalida(mAdc)
         
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
                        
def getFimDoJogo():
        global fimDoJogo
        return fimDoJogo
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
   
                if(getPecaAtPosicao(xIni+1,yIni-1)=="o" or getPecaAtPosicao(xIni+1,yIni-1)=="O" ) and yIni>0:
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni-1
            
                if(getPecaAtPosicao(xIni-1,yIni+1)=="o" or getPecaAtPosicao(xIni-1,yIni+1)=="O" ) and xIni>0:
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni+1
                
                if(getPecaAtPosicao(xIni-1,yIni-1)=="o" or getPecaAtPosicao(xIni-1,yIni-1)=="O" ) and(xIni>0 and yIni>0):
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni-1
        if(jogador=="C"):
                if(getPecaAtPosicao(xIni+1,yIni+1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" )and xIni>0:
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni+1
                if(getPecaAtPosicao(xIni+1,yIni-1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" )and yIni>0:
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni-1
                if(getPecaAtPosicao(xIni-1,yIni+1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" ):
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni+1
                if(getPecaAtPosicao(xIni-1,yIni-1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" ) and(xIni>0 and yIni>0):
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni-1
        if(deveComer):
                showJogadaInvalida("Você Deve comer a peça na posição "+pegarLetraTabela(xInipos)+","+str(yInipos))
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
def contarPecasJogadorDeCima():
        global posicoes;
        j=0
        for i in range(len(posicoes)):
                if(posicoes[i]=="o" or posicoes=="O"):
                        j+=1;  
        return j;     
def contarPecasJogadorDeBaixo():
        j=0
        for i in range(len(posicoes)):
                if(posicoes[i]=="@" or posicoes=="&"):
                        j+=1;      
        return j;      


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
                showJogadaInvalida("")

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
def zerarPecasCima():
        for i in range(len(posicoes)):
                if(posicoes[i]=="o" or posicoes=="O"):
                        posicoes[i]=" ";
def zerarPecasBaixo():
        for i in range(len(posicoes)):
                if(posicoes[i]=="@" or posicoes=="&"):
                        posicoes[i]=" ";


def testar():
        inicializar()
        
        fazerJogada("B","B6--C5")
        fazerJogada("B","C5--B4")
        fazerJogada("C","D2--C3")
        fazerJogada("C","C3--D4")