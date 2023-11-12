from math import *
st = input()
l = len(st)
a = -(l-1)//2
b = (l-1)//2
for i in range(a,b+1):
    for j in range(abs(i)):
        print(" ",end="")
    for j in range(abs(i),l-abs(i)):
        print(st[j],end="")