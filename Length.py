import math

print('BOOM tetris for jeff')
eq = int(input("What type of function? 1 for polyomial, 2 for exponential, 3 for trignometric, 4 for logarithm"))
lower= float(input('what is the lower bound of your arc length?: '))
higher = float(input("What is the upper bound of your arc length?: "))

if eq == 1:
    print("ax^b + c")
    a=float(input("what is a?: "))
    b=float(input("what is b?: "))
    c=input("what is c?: ")
    ab=a*b
    bmin=b-1
    
if eq == 2:
    print("ab^x+c")
    ae=float(input("what is a?: "))
    be=float(input("what is b?: "))
    ce=input("what is c?: ")
    
if eq == 3:
    print("a(trig(b))+c")
    at=float(input("what is a?: "))
    tt=float(input("what trig function? 1=sin, 2=cos, 3=tan: "))
    bt=float(input("what is b?: "))
    ct=float(input("what is c?: "))
