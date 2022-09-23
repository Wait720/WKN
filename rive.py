import math
x=float(input("x="))
if x>3 and x!=6:
    y=2.31-math.log10(abs(x-6))
    
elif 0<=x<=3:
    y=math.cos(x+3)+math.sin(2*x+math.pi/2)
    
else:
    y=3/x+pow(math.e,x)/pow(x,3)
print(("f(x)="),y)
