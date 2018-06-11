import math

print('BOOM tetris for jeff')
eq = int(input("What type of function? 1 for polynomial, 2 for exponential, 3 for trignometric, 4 for logarithm"))

if eq == 1:
    print("ax^b + c")
    ap=float(input("what is a?: "))
    bp=float(input("what is b?: "))
    cp=input("what is c?: ")
    #Taking Derivative Here
    ab=ap*bp
    bmin=bp-1
    print("f'(x)= ",ab, "x^", bmin)
    #Squaring the Derivative here
    absqr=ab*ab
    bsqr=bmin*2
    print("(f'(x))^2= ",absqr,"x^",bsqr)
    
if eq == 2:
    print("ab^x+c")
    ae=float(input("what is a?: "))
    be=float(input("what is b?: "))
    ce=input("what is c?: ")
    
if eq == 3:
    print("a(trig(b))+c")
    at=float(input("what is a?: "))
    tt=int(input("what trig function? 1=sin, 2=cos, 3=tan: "))
    bt=float(input("what is b?: "))
    ct=float(input("what is c?: "))

if eq == 4:
    print("a(logBASE(b))+c")
    al=float(input("what is a?: "))
    ll=float(input("what log base?: "))
    bl=float(input("what is b?: "))
    cl=float(input("what is c?: "))


def f(x):
    return math.sqrt(((absqr*x)**bsqr)+1)

def LEN (a,b,n):
    h = (b-a)/n
    x = a
    i = 1
    
    MRAM = 0.0
    for i in range(n):
        if x==b:
            print("i=",i)
        else:
            x1 = a + (i+1)*h
            MRAM = MRAM + f((x+x1)/2)*h
            x=x1
    return "MRAM = {}.".format(MRAM)


def main():
    a = int(input("what is the lower bound of your arc length?: "))
    b = int(input("what is the upper bound of your arc length?: "))
    n = int(input("Number of Subintervals: "))
    print(LEN(a,b,n))

main()

