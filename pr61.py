import math
a=float(input("a="))
b=float(input("b="))
h=float(input("h="))
def ff(x):
    z=math.log(abs(2*x+7))+pow(x,1/3)-pow(x,1/3)
    return(z)
for i in range(30):
    y=ff(a)
    print(i,'  ',a,'  ',y )
    a=a+h
    if a>b:
        break