def separar():
    print("",end=" ")
    for i in range(21):
        if(i%2==0):
            print("+",end="")
        else:
            print("-",end="")
    #print("\n")
def desenharLetras():
    letras=["A","B","C","D","E","F","G","H","I","J"]
    c=0;
    print("  ",end='')
    for i in range(20):
        if(i%2==1):
            print(letras[c],end=" ")
            c+=1;
    print()
def renderizar():
    
    desenharLetras()    
    #print("")  
    separar()
    print()   
    for y in range(10):
        print(y,end="")
        
        for x in range(10):
            print("| ",end="")
            
        print("|")
        separar()   
        print() 
       
        
    desenharLetras()

renderizar()
