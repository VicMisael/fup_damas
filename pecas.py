import render;

posicoes=[" "]*100;
pecasPadrao=["o","@"]
pecasDama=["O","&"]




for i in range(100):
    if((i//10)%2==0):
        if(i%2==0):
            posicoes[i]="#";
    else:
        if(i%2==1):
            posicoes[i]="#";


for a in range(30):
    print(a)
    if(posicoes[a]!="#"):
        posicoes="o"

board.renderizar(posicoes)
