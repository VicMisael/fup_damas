#Arquivo somente para renderizar o tabuleiro e controlar ele, nada de mais importante aqui
import os;
from colorama import Fore,Back,Style;
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
    print(Fore.RED+"  jogada inválida \n "+mAdicional)
    print(Style.RESET_ALL)
def venceu(mensagem):
    limpar();
    print(Fore.GREEN+mensagem)
    print(Style.RESET_ALL)

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

