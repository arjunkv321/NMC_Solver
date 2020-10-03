import math
from sympy import *

x=Symbol('x')
e=sympify(input("Enter function in x: ")) #enter function
expression=e.subs({'x':x})
f=lambdify(Symbol('x'),expression,'numpy')
a=float(input("Enter initial value of range : "))         #input range
b=float(input("Enter final value of range : "))
# while True
#     a=float(input("Enter initial value of range : "))         #input range
#     b=float(input("Enter final value of range : "))
#     if a>b or f(a)*f(b)>1:
#         print("Invalid , Enter again")
#     else:
#         break
num_iter=int(input("Enter number of iteration: "))         #enter number of iteration
round_of=int(input("Enter round of number :"))          #enter the number of iteration
c=0
dictx={}

for i in range(num_iter):
    q=c
    c=(a+b)/2
    dictx[i]=dictx.get(i,[round(a,round_of),round(b,round_of),round(c,round_of),round((f(c)),round_of),abs(round((q-c)/c*100,round_of))])
    # print("Sl.No {:<10} a={:<12} b={:<12} c={:<12} f(c)={:<20} epsa={:<12}".format(i,round(a,round_of),round(b,round_of),round(c,round_of),round((f(c)),round_of),abs(round((q-c)/c*100,round_of))))
    if (f(c))<0:
        a=c
    else:
        b=c
print("\n\n\n")
print(dictx)
print(dictx[0][1])

while True:
    y=input("Enter 'q' to exit : ")
    if y=="q" or y=="Q":
        break
