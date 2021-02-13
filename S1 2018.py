N = int(input())

villages = []


for i in range(N):
    village = {}
    village = int(input())
    villages.append(village)

villages.sort()
min_vill = None

for i in range(len(villages)):

    if i == 0:
        continue
    elif i == (len(villages) - 1):
        continue
    
    else:
        leftdistance = villages[i] - ((villages[i]+ villages[i-1]) / 2)
        rightdistance = ((villages[i]+ villages[i+1]) / 2) - villages[i]
        vill_size = leftdistance + rightdistance

        if min_vill == None:
            min_vill = vill_size
            
        if vill_size < min_vill: 
            min_vill = vill_size

print (min_vill)
    


    
    
    
