import render;
posicoes=[" "]*100;
pecasPadrao=["o","@"]
pecasDama=["O","&"]


#Vai inicializar o tabuleiro e colocar as peças nas suas posições padrões
def inicializar():
        for i in range(100):
                if((i//10)%2==0):
                        if(i%2==0):
                                posicoes[i]="#";
                else:
                        if(i%2==1):
                                posicoes[i]="#";
        for a in range(30):
                if(posicoes[a]!="#"):
                        posicoes[a]=pecasPadrao[0];
        a=0
        for a in range(60,100):
                if(posicoes[a]!="#"):
                        posicoes[a]=pecasPadrao[1];
        render.renderizar(posicoes)
def fazerJogada(jogador,jogada):
        if(jogador=="C"):
                print("O Jogador de cima foi o Selecionado")
        if(jogador=="B"):
                print("O jogador de baixo foi selecionado");
        vetJog=jogada.split("--")
        endInicial=pegarEnderecoDaTabela(vetJog[0]);
        endFinal=pegarEnderecoDaTabela(vetJog[1]);
        print(endInicial);
        print(endFinal)

def pegarEnderecoDaTabela(endereco):
        #Vai traduzir o endereço da coluna para numeros,para tornar o acesso ao vetor de peças mais fácil
        endY=int(endereco[1])
        endX=-1;
        letra=endereco[0];
        letra=letra.upper();
        print(letra)
        if letra=="A":
                endX=0;
        elif letra=="B":
                endX=1;
        elif letra=="C":
                endX=2
        elif letra=="D":
                endX=3
        elif letra=="E":
                endX=4;
        elif letra=="F":
                endX=5
        elif letra=="G":
                endX=6;
        elif letra=="H":
                endX=7;
        elif letra=="I":
                endX=8;
        elif letra=="J":
                endX=9;
        else:
                print("posição invalida")
        if(endY>9):
                print("Posição invalida")
        end=[endX,endY]  
        return end;

         
        