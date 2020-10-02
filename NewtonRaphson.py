import sympy
from sympy import *
import math

x=Symbol('x')
e=sympify(input("Enter function in x: "))
expression=e.subs({'x':x})
f=lambdify(Symbol('x'),expression,'numpy')
fprime=diff(expression)
deriv=lambdify(Symbol('x'),fprime,'numpy')

initial_x=float(input("Enter initial Value: "))
num_iter=int(input("Enter number of iteration: "))
round_of=int(input("Enter round of number :"))
c=0

def eq(x):
    ans=x-(f(x)/deriv(x))
    return(ans)

print("x0 = {}".format(initial_x))
for i in range(num_iter):
    c=eq(initial_x)
    print("x{} = {:<12}".format(i+1,round(c,round_of)))
    initial_x=c

while True:
    y=input("Enter 'q' to exit : ")
    if y=="q" or y=="Q":
        break
