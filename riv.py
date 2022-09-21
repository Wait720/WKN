import math
x=float(input("Введіть х:"))
y=float(input("Введіть у:"))
def w(x,y):
    print(math.sin(x)-math.cos(y)*4.138*math.log(abs(math.sin(math.pi/4+2.31*x))))
w(x,y)
