import math
import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
h=float(sys.argv[3])
a1=abs(0-a)+h
b1=math.sqrt(math.pow(h,2)+math.pow(a,2))
c=math.sqrt(math.pow(h,2)+math.pow(a,2))
print(a,b,h)
print("Сторона АС:",a1)
print("Сторона АВ:",b1)
print("Сторона ВС:",c)




