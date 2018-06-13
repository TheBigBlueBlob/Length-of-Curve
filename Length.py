import math

print('BOOM tetris for jeff')
eq = int(input("What type of function? 1 for polynomial, 2 for exponential, 3 for logarithm,"))

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
    nata= ae*math.log(be)
    print("f'(x)=",nata, be, "^x")
    natasq=nata*nata
    print("(f'(x))^2=", natasq, be, "^2x")

if eq == 3:
    print("a(logBASE(x))+c")
    al=float(input("what is a?: "))
    bl=float(input("what BASE? "))
    cl=float(input("what is c?: "))
    derl = al/(math.log(bl))
    print("f'(x)=",derl,"/x")
    dersq= derl*derl
    print("(f'(x))^2 =",dersq,"/x^2")
    
def f(x):
    return math.sqrt((absqr*(x**bsqr))+1)

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

def f(y):
    return math.sqrt(natasq*(be**(2*y))+1)

def ENG (a2,b2,n2):
    h2 = (b2-a2)/n2
    y = a2
    i2 = 1
    
    MRAM2 = 0.0
    for i2 in range(n2):
        if y==b2:
            print("i=",i2)
        else:
            x2 = a2 + (i2+1)*h2
            MRAM2 = MRAM2 + f((y+x2)/2)*h2
            y=x2
    return "MRAM = {}.".format(MRAM2)


def main2():
    a2 = int(input("what is the lower bound of your arc length?: "))
    b2 = int(input("what is the upper bound of your arc length?: "))
    n2 = int(input("Number of Subintervals: "))
    print(ENG(a2,b2,n2))

def f(z):
    return math.sqrt(((dersq)/(z*z))+1)

def LOG (a3,b3,n3):
    h3 = (b3-a3)/n3
    z = a3
    i3 = 1
    
    MRAM3 = 0.0
    for i3 in range(n3):
        if z==b3:
            print("i=",i3)
        else:
            x3 = a3 + (i3+1)*h3
            MRAM3 = MRAM3 + f((z+x3)/2)*h3
            z=x3
    return "MRAM = {}.".format(MRAM3)


def main3():
    a3 = int(input("what is the lower bound of your arc length?: "))
    b3 = int(input("what is the upper bound of your arc length?: "))
    n3 = int(input("Number of Subintervals: "))
    print(LOG(a3,b3,n3))

if eq == 1:
    main()
if eq == 2:
    main2()
if eq == 3:
    main3()

