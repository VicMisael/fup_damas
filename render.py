def separar():
    for i in range(21):
        if(i%2==0):
            print("+",end=" ")
        else:
            print("-",end=" ")
    #print("\n")
def desenharLetras():
    print("")
    letras=["A","B","C","D","E","F","G","H","I","J"]
    c=0;
    for i in range(20):
        print("",end=" ")
        if(i%2==1):
            print(letras[c],end=" ")
            c+=1;
    print("")
def renderizar():
    
    desenharLetras()    
    #print("")  
    #separar()   
    for y in range(10):
        separar()   
       
       
        
    desenharLetras()

renderizar()
