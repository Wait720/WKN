import math
x=float(input("Введіть х"))
y=pow(math.e, 9/10*x+4)+pow(x, 1/2)+2*pow(x, 2/4)/6*(abs(x+2)+1)
b=9*math.cos(7/10*x+math.sqrt(x))
x1=y-b
print("f(x)=", x1)
