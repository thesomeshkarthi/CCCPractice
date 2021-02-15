N = int(input())
Scount = []
Tcount = []

for i in range(N):
    line = input()
    S = line.count('S') + line.count('s')
    T = line.count('T') + line.count('t')
    Scount.append(S)
    Tcount.append(T)


Ssum = sum(Scount)
Tsum = sum(Tcount)

if Ssum >= Tsum:
    print("French")
else:
    print ("English")


    


    
    
