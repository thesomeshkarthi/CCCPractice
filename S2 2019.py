N = int(input())
number = []
primeNumbers = []
numbersSelected = "false"

for i in range(N):
    line = int(input()) * 2
    number.append(line)


for x in range(len(number)):
    numbersSelected = "false"
    primeNumbers.clear()

    for y in range(number[x]):
        if y > 1:
            for z in range(2, y):
                if(y % z) == 0:
                    break
            else:
                primeNumbers.append(y)

    for i in range(len(primeNumbers)):
        for j in range(len(primeNumbers)):
            if primeNumbers[i] + primeNumbers[j] == number[x]:
                if (numbersSelected == "false"):
                    print(str(primeNumbers[i]) + " " + str(primeNumbers[j]))
                    numbersSelected = "true" 
                

                
                
        



    

