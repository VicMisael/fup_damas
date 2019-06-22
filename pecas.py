import render
import math
fimDoJogo=False
posicoes=[" "]*100
pecasPadrao=["o","@"]
pecasDama=["O","&"]
scores=[0,0]
jogadaInvalida=False;
proximoJogador=False;
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
        global proximoJogador
        try:
                vetJog=jogada.split("--")
                endInicial=pegarEnderecoDaTabela(vetJog[0])
                endFinal=pegarEnderecoDaTabela(vetJog[1])
        except:
                
                render.mostrarErro("Erro ao inserir a jogada");
                render.renderizar(posicoes);
                return False;
        proximoJogador=False;
        render.limpar();
        if endInicial[0]==-1 or endInicial[1]==-1  or endFinal[0]==-1 or endFinal[1]==-1:
                showJogadaInvalida("")
                return False
        (x1,y1)=endInicial
        (x2,y2)=endFinal
        distancia = getDistancia(x1, y1, x2, y2)

        if getPecaAtPosicao(x1,y1)=="#" or getPecaAtPosicao(x2,y2)=="#" or getPecaAtPosicao(x1,y1)==" " :
                showJogadaInvalida("Não é possível mover uma peça vazia ou mover para ou de uma divisoria do tabuleiro ")
                render.renderizar(posicoes);
                return False
        elif(distancia==-1):
                showJogadaInvalida("Movimentos somente em diagonais")
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
                        else:
                                showJogadaInvalida("Você só pode mover a peça do seu jogador")
                                
                if(distancia==2 and not (getPecaAtPosicao(x1,y1)=="O" or getPecaAtPosicao(x1,y1)=="&")):
                        #Como pra comer uma peça a distancia tem de ser 2,vai checar a peça do meio e comer e contar o placar
                        if jogador=="B" and ((getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="o") or getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="O") and getPecaAtPosicao(x2,y2)==" "  :
                                comerPeca(jogador,"N",(x1+x2)//2,(y1+y2)//2)
                                moverPeca(x1, y1, x2, y2)
                        elif jogador=="C" and (getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="@" or getPecaAtPosicao((x1+x2)//2,(y1+y2)//2)=="&") and getPecaAtPosicao(x2,y2)==" ":
                                comerPeca(jogador, "N", (x1+x2) // 2, (y1+y2) // 2)
                                moverPeca( x1, y1, x2, y2)
                        else:
                                showJogadaInvalida("Não é possível comer dessa maneira")
                elif(distancia>=2):
                        
                        if(getPecaAtPosicao(x1,y1)=="&") or (getPecaAtPosicao(x1,y1)=="O"):
                               # showJogadaInvalida(checarDiagonaisDama(x1,y1,jogador));
                                if((jogador=="C" and getPecaAtPosicao(x1,y1)=="O") or (jogador=="B" and getPecaAtPosicao(x1,y1)=="&")):
                                        if(checarPecasEComerComDamas(x1,y1,x2,y2,jogador)):
                                                moverPeca(x1,y1,x2,y2)
                                        else:
                                                showJogadaInvalida("Não é possivel comer mais de uma peça com damas")
                                else:
                                        showJogadaInvalida("Você não pode jogar as peças de seu adversário")
                        else:
                                showJogadaInvalida("Só se move mais de duas casas as damas")

                #vai checar se alguma peça pode se tornar dama
                for i in range(10):
                        if(getPecaAtPosicao(i,9)=="o"):
                                setPecaAtPosicao("O",i,9)
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
#Essas de baixo aq tão obviasBs
def retornarValidezDaJogada():
        global jogadaInvalida
        return jogadaInvalida
def showJogadaInvalida(mAdc):
        global jogadaInvalida
        jogadaInvalida=True;
        render.showJogadaInvalida(mAdc)
def checarDiagonaisDama(x1,y1,Jogador):
        xAux=x1
        yAux=y1
        npecascomiveis=0
        if(Jogador=="B"):
                while(not(xAux==0 or yAux==0)):
                        if(getPecaAtPosicao(xAux,yAux)=="o" or getPecaAtPosicao(xAux,yAux)=="O"):
                                npecascomiveis+=1;
                        xAux-=1
                        yAux-=1
                while(not(xAux==9 or yAux==9)):
                        if(getPecaAtPosicao(xAux,yAux)=="o" or getPecaAtPosicao(xAux,yAux)=="O"):
                                npecascomiveis+=1;
                        xAux+=1;
                        yAux+=1;
                while(not(xAux==9 or yAux==0)):
                        if(getPecaAtPosicao(xAux,yAux)=="o" or getPecaAtPosicao(xAux,yAux)=="O"):
                                npecascomiveis+=1;
                        xAux+=1
                        yAux-=1
                while(not(xAux==0 or yAux==9)):
                        if(getPecaAtPosicao(xAux,yAux)=="o" or getPecaAtPosicao(xAux,yAux)=="O"):
                                npecascomiveis+=1;
                        xAux-=1
                        yAux+=1
        if(Jogador=="C"):
                while(not(xAux==0 or yAux==0)):
                        if(getPecaAtPosicao(xAux,yAux)=="@" or getPecaAtPosicao(xAux,yAux)=="&"):
                                npecascomiveis+=1;
                        xAux-=1
                        yAux-=1
                while(not(xAux==9 or yAux==9)):
                        if(getPecaAtPosicao(xAux,yAux)=="@" or getPecaAtPosicao(xAux,yAux)=="&"):
                                npecascomiveis+=1;
                        xAux+=1;
                        yAux+=1;
                while(not(xAux==9 or yAux==0)):
                        if(getPecaAtPosicao(xAux,yAux)=="@" or getPecaAtPosicao(xAux,yAux)=="&"):
                                npecascomiveis+=1;
                        xAux+=1
                        yAux-=1
                while(not(xAux==0 or yAux==9)):
                        if(getPecaAtPosicao(xAux,yAux)=="@" or getPecaAtPosicao(xAux,yAux)=="&"):
                                npecascomiveis+=1;
                        xAux-=1
                        yAux+=1
        return npecascomiveis

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
        elif(npecascomiveis==1):
                comerPeca(jogador,"N",pecaPosX,pecaPosY)
                global proximoJogador
                proximoJogador=False
        else:
                proximoJogador=True;

        return not jogadaProibida
                        
def getFimDoJogo():
        global fimDoJogo
        return fimDoJogo
def checarPecasAoRedor(xIni,yIni,jogador):
        #print("A ser implementada")       
        deveComer=False;
        xInipos=-1;
        yInipos=-1;
        if(jogador=="B"):
                if(getPecaAtPosicao((xIni+1),(yIni+1))=="o" or getPecaAtPosicao((xIni+1),(yIni+1))=="O") and getPecaAtPosicao(xIni+2,yIni+2)==" ":
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni+1
   
                if(getPecaAtPosicao(xIni+1,yIni-1)=="o" or getPecaAtPosicao(xIni+1,yIni-1)=="O" ) and yIni>0 and getPecaAtPosicao(xIni+2,yIni-2)==" ":
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni-1
            
                if(getPecaAtPosicao(xIni-1,yIni+1)=="o" or getPecaAtPosicao(xIni-1,yIni+1)=="O" ) and xIni>0 and getPecaAtPosicao(xIni-2,yIni+2)==" ":
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni+1
                
                if(getPecaAtPosicao(xIni-1,yIni-1)=="o" or getPecaAtPosicao(xIni-1,yIni-1)=="O" ) and(xIni>0 and yIni>0) and getPecaAtPosicao(xIni-2,yIni-2)==" ":
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni-1
        if(jogador=="C"):
                if(getPecaAtPosicao(xIni+1,yIni+1)=="@" or getPecaAtPosicao(xIni+1,yIni+1)=="&" )and getPecaAtPosicao(xIni+2,yIni+2)==" ":
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni+1
                if(getPecaAtPosicao(xIni+1,yIni-1)=="@" or getPecaAtPosicao(xIni+1,yIni-1)=="&" )and yIni>0 and getPecaAtPosicao(xIni+2,yIni-2)==" ":
                        deveComer=True;
                        xInipos=xIni+1
                        yInipos=yIni-1
                if(getPecaAtPosicao(xIni-1,yIni+1)=="@" or getPecaAtPosicao(xIni-1,yIni+1)=="&" )and xIni>0 and getPecaAtPosicao(xIni-2,yIni+2)==" ":
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni+1
                if(getPecaAtPosicao(xIni-1,yIni-1)=="@" or getPecaAtPosicao(xIni-1,yIni-1)=="&" ) and(xIni>0 and yIni>0)and getPecaAtPosicao(xIni-2,yIni-2)==" ":
                        deveComer=True;
                        xInipos=xIni-1
                        yInipos=yIni-1
        if(xInipos==9 or xInipos==0):
                deveComer=False  

        if(deveComer):
                showJogadaInvalida("Você Deve comer a peça na posição "+pegarLetraTabela(xInipos)+","+str(yInipos))
        return not deveComer
def setPecaAtPosicao(peca,x,y):
        global posicoes
        posicoes[x+y*10]=peca
def getPecaAtPosicao(x,y):
        if(not (x>9 or y>9)):
                return posicoes[x+y*10]
        else:
                return " "
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
        #print(endereco)
        if(str(endereco[1]).isdigit):
                endY=int(endereco[1])
        else:
                endY=-1;
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
def pegarScore():
        global scores;
        return scores;
def testeLimparCima():
        for i in range(len(posicoes)):
                if(posicoes[i]=="O" or posicoes[i]=="o"):
                        posicoes[i]==" "
def testar():
        #Função que existe só pra fazer testes
        inicializar()
        
        fazerJogada("B","J6--I5")
        fazerJogada("C","J2--I3")
        fazerJogada("B","I5--J4")
        
        fazerJogada("C","H2--G3")
        fazerJogada("B","B6--C5")
#testar();