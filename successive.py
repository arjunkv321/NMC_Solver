import math
from sympy import *
import math

x=Symbol('x')
e=sympify(input("Enter function in f(x) ( convert by yourself in format x=f(x)): "))
expression=e.subs({'x':x})
f=lambdify(Symbol('x'),expression,'numpy')

initial_x=float(input("Enter initial Value: "))
num_iter=int(input("Enter number of iteration: "))
round_of=int(input("Enter round of number :"))
c=0

print("x0 = {}".format(initial_x))
for i in range(num_iter):
    c=f(initial_x)
    print("x{} = {}".format(i+1,round(c,round_of)))
    initial_x=c

while True:
    y=input("Enter 'q' to exit : ")
    if y=="q" or y=="Q":
        break
