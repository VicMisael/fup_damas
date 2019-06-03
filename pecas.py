import render
posicoes=[" "]*100
pecasPadrao=["o","@"]
pecasDama=["O","&"]
scores=[0,0]

#Vai inicializar o tabuleiro e colocar as peças nas suas posições padrões
def inicializar():
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
        if(jogador=="C"):
                print("O Jogador de cima foi o Selecionado")
        if(jogador=="B"):
                print("O jogador de baixo foi selecionado")
        vetJog=jogada.split("--")
        endInicial=pegarEnderecoDaTabela(vetJog[0])
        endFinal=pegarEnderecoDaTabela(vetJog[1])
        if(endInicial[0]==-1 or endInicial[1]==-1  or endFinal[0]==-1 or endFinal[1]==-1):
                print("Posição invalida")
                return
        (x1,y1)=endInicial
        (x2,y2)=endFinal
        if getPecaAtPosicao(x1,y1)=="#" or getPecaAtPosicao(x2,y2)=="#" :
                print("Jogada invalida #")
        distancia=getDistancia(x1,y1,x2,y2)
        if(distancia==-1 or (distancia>2 and (getPecaAtPosicao(x1,y1)!="O" or getPecaAtPosicao(x1,y1))!="&")):
                print("Jogada inválida distancia")
        else:
                if(distancia==1):
                        moverPeca(jogador,x1,y1,x2,y2)



                #vai checar se alguma peça pode se tornar dama
                for i in range(10):
                        if getPecaAtPosicao(i,9)=="o":
                                setPecaAtPosicao("O",i,9)
                for i in range(10):
                        if getPecaAtPosicao(i, 0) == "@":
                                setPecaAtPosicao("&", i, 9)
        print(scores)
        render.renderizar(posicoes)
#Essas de baixo aq tão obvias
def setPecaAtPosicao(peca,x,y):
        posicoes[x+y*10]=peca
def getPecaAtPosicao(x,y):
        return posicoes[x+y*10]

def comerPeca(jogador,modo,x,y):
       if(modo=="N"):
               setPecaAtPosicao(" ",x,y)
               if jogador == "B":
                       scores[0] += 1;





def moverPeca(jogador,x1,y1,x2,y2):
        if (jogador == "B"):
                if (getPecaAtPosicao(x1, y1) == "@" and getPecaAtPosicao(x2, y2) == " "):
                        setPecaAtPosicao("@", x2, y2)
                        setPecaAtPosicao(" ", x1, y1)

        if (jogador == "C"):
                if (getPecaAtPosicao(x1, y1) == "o" and getPecaAtPosicao(x2, y2) == " "):
                        setPecaAtPosicao("o", x2, y2)
                        setPecaAtPosicao(" ", x1, y1)

def getDistancia(x1,y1,x2,y2):
        #vai pegar a distancia percorrida pela peça
      distX=((x1-x2)**2)**0.5
      distY=((y1-y2)**2)**0.5
      if distX==distY:
        return distX
      else:
              return -1;  
        



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

         
        