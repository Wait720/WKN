import math
x=int(input("x="))
if x>3:
    y1=2.31-math.log10(abs(x-6))
    print(("f(x)=",y1))
elif 0<=x<=3:
    y2=math.cos(x+3)+math.sin(2*x+math.pi/2)
    print(("f(x)="),y2)
else:
    y3=3/x+pow(math.e,x)/pow(x,3)
    print(("f(x)="),y3)

