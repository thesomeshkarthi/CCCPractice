n1 = int(input())
n2 = int(input())
num = []


for i in range ((n2 - n1) + 1):
    x = float(n1 + i)
    sqrtx = x **(1/2)
    cubex = round(x **(1/3.), 3)
    if cubex.is_integer() == True:
        if sqrtx.is_integer() == True:
            num.append(x)


print(len(num))





    


        


