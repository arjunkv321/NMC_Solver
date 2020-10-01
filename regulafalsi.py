import math
a=0
b=1
z=11
c=0
r=6
def eq(x):
    fx=x*math.exp(x)-1
    return(fx)
for i in range(z):
    q=c
    c=round(b-(eq(b)*(a-b)/(eq(a)-eq(b))),r)
    print("Sl.No {:<10} a={:<12} b={:<12} c={:<12} f(c)={:<20} epsa={:<12}".format(i,round(a,r),round(b,r),round(c,r),round((eq(c)),r),abs(round((q-c)/c*100,r))))
    if (eq(c))<0:
        a=c
    else:
        b=c
