one=int(input("組數為:"))
a=[]
for i in range(one):
    b,c=map(int,input("第"+str(i+1)+"組:").split())
    d=b*250+c*175
    a.append(d)
for i in range(one):
    print("第",i+1,"組應收費用:",a[i])