#Arquivo somente para renderizar o tabuleiro, nada de mais importante aqui
def separar():
    print("",end=" ")
    for i in range(21):
        if(i%2==0):
            print("+",end="")
        else:
            print("-",end="")
def desenharLetras():
    letras=["A","B","C","D","E","F","G","H","I","J"]
    c=0;
    print("  ",end='')
    for i in range(20):
        if(i%2==1):
            print(letras[c],end=" ")
            c+=1;
    print()
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

