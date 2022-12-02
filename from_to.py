#!/usr/bin/env python

##############################
# --- Ich bin kein Virus --- #
##############################

a = int(input("Enter Number: "))
b = int(input("Enter Original Base: "))
c = int(input("Enter Future Base: "))

def to_dec(a,b):
    s = 0
    if a==0:
        return print(0)
    i=0
    while a>0:
        c=a%10
        a-=c
        a/=10
        if c>=b:
            print("Input Error")
            quit()
        s+=pow(b,i)*c
        i+=1
    return s

def to_bin(a,b):
    s = ""
    if a==0:
        return print(0)
    while a>0:
        c=a%b
        a-=c
        a/=b
        s=format(str(int(c))+s)
    print(s)

if c<2:
    print("Input Error")
    quit()
s=to_dec(a,b)
to_bin(s,c)
