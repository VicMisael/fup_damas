#Arquivo somente para renderizar o tabuleiro e controlar ele, nada de mais importante aqui
import os;
def separar():
    print("",end=" ")
    for i in range(21):
        if(i%2==0):
            print("+",end="")
        else:
            print("-",end="")
def desenharLetras():
    letras=["A","B","C","D","E","F","G","H","I","J"]
    c=0
    print("  ",end='')
    for i in range(20):
        if(i%2==1):
            print(letras[c],end=" ")
            c+=1
    print()
def showJogadaInvalida(mAdicional):
    limpar()
    vermelho="\033[1;31;40m"
    reset=" \033[m"
    print(vermelho+"  jogada inválida \n "+mAdicional+ reset)
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
def renderizar(board):
    desenharLetras()    
    #print("")  
    separar()
    print()   
    for y in range(10):
        print(y,end="")
        #Para cada linha desenha 10 colunas
        for x in range(10):
            print("|",end="")
            print(board[x+y*10],end="")
            #Desenhe os objetos no array board
            #multiplicado por 10 pois são as linhas
        print("|")
        separar()   
        print() 
    #chamar print vazio toda vez que for necessario fazer uma quebra de linha
        
    desenharLetras()

