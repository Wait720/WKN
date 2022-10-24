import math
import random
s=float(input("найменше значення х = "))
d=float(input("найбільше значення х = "))
h=float(input("h="))
x=s
spisok=[]
def f():
    a=math.log(abs(2*x+7))+pow(x,1/3)-pow(x,1/3)
    spisok.append(a)
while x<=d:
    f()
    x=x+h
random.shuffle(spisok)
print(spisok)

