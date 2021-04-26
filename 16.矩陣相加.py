one=map(int,input("").split())
one1=map(int,input("").split())
one2=map(int,input("").split())
two=map(int,input("").split())
two1=map(int,input("").split())
two2=map(int,input("").split())
a=list(one)
b=list(one1)
c=list(one2)
d=list(two)
e=list(two1)
f=list(two2)
if a==d:
    for i in range(len(b)):
        print(b[i]+e[i],end=" ")
    print()
    for i in range(len(b)):
        print(c[i]+f[i],end=" ")
else:
    print("兩個矩陣無法相加")
