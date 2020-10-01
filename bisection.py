import math
a=1
b=2
r=6
z=11
c=0

def eq(x):
    fx=x**3-x-1
    return(fx)
for i in range(z):
    q=c
    c=round((a+b)/2,r)
    print("a={:<12} b={:<12} c={:<12} f(c)={:<20} epsa={:<12}".format(round(a,r),round(b,r),round(c,r),round((eq(c)),r),abs(round((q-c)/c*100,r))))
    if (eq(c))<0:
        a=c
    else:
        b=c
