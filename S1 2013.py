def uniqueYear(N):
    year = str(N)
    
    for i in range(len(year)):
        for j in range(i + 1,len(year)):
            if(year[i] == year[j]):
                return False;

    return True;


            
N = int(input())
yearReached = "false"

while yearReached == "false":
    N = N+1
    if (uniqueYear(N)):
        print(N)
        yearReached = "true"
    else:
        continue

    


    
    
    


 


    
