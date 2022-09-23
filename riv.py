import math
x1=float(input("Введіть х:"))
y1=float(input("Введіть у:"))
def w(x,y):
    print(math.sin(x)-math.cos(y)*4.138*math.log(abs(math.sin(math.pi/4+2.31*x))))
w(x1,y1)
