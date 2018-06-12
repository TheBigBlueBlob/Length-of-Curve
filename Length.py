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
    nata= ae*math.log(be)
    print("f'(x)=",nata, be, "^x")
    natasq=nata*nata
    print("(f'(x))^2=", natasq, be, "^2x")
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
    return math.sqrt(natasqr*(be**(2*y))+1)

def ENG (2a,2b,2n):
    2h = (2b-2a)/2n
    y = 2a
    2i = 1
    
    2MRAM = 0.0
    for 2i in range(2n):
        if y==2b:
            print("i=",2i)
        else:
            x2 = 2a + (2i+1)*2h
            2MRAM = 2MRAM + f((y+x2)/2)*2h
            y=x2
    return "MRAM = {}.".format(2MRAM)


def 2main():
    2a = int(input("what is the lower bound of your arc length?: "))
    2b = int(input("what is the upper bound of your arc length?: "))
    2n = int(input("Number of Subintervals: "))
    print(ENG(2a,2b,2n))
"""
def 3f():
    return math.sqrt((absqr*(x**bsqr))+1)

def 3LEN (3a,3b,3n):
    3h = (3b-3a)/3n
    3x = 3a
    3i = 1
    
    3MRAM = 0.0
    for 3i in range(3n):
        if 3x==3b:
            print("i=",3i)
        else:
            x3 = 3a + (3i+1)*3h
            3MRAM = 3MRAM + 3f((3x+x3)/2)*3h
            3x=x3
    return "MRAM = {}.".format(3MRAM)


def 3main():
    3a = int(input("what is the lower bound of your arc length?: "))
    3b = int(input("what is the upper bound of your arc length?: "))
    3n = int(input("Number of Subintervals: "))
    print(3LEN(3a,3b,3n))

def 4f(x):
    return math.sqrt((absqr*(x**bsqr))+1)

def 4LEN (4a,4b,4n):
    4h = (4b-4a)/4n
    4x = 4a
    4i = 1
    
    4MRAM = 0.0
    for 4i in range(4n):
        if 4x==4b:
            print("i=",4i)
        else:
            x4 = 4a + (4i+1)*4h
            4MRAM = 4MRAM + 4f((4x+x4)/2)*4h
            4x=x4
    return "MRAM = {}.".format(4MRAM)


def 4main():
    4a = int(input("what is the lower bound of your arc length?: "))
    4b = int(input("what is the upper bound of your arc length?: "))
    4n = int(input("Number of Subintervals: "))
    print(4LEN(4a,4b,4n))
"""
if eq == 1:
    main()
if eq == 2:
    2main()
"""
if eq == 3:
    3main()
if eq == 4:
    4main()
"""
