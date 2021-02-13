N = str(input())
flips = []


for i in range(len(N)):
    flip = {}
    flip = N[i]
    flips.append(flip)


array = ["1", "2", "3", "4"]


for flip in flips:
    flipType = flip
    array0value = array[0]
    array1value = array[1]
    array2value = array[2]
    array3value = array[3]

    
    if flipType == "H":
        array[0] = array2value
        array[1] = array3value
        array[2] = array0value
        array[3] = array1value

    if flipType == "V":
        array[0] = array1value
        array[1] = array0value
        array[2] = array3value
        array[3] = array2value

print (array[0] + " " + array[1])
print (array[2] + " " + array[3])
        
    
