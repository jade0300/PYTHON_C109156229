n,m=map(int,input("輸入N及M為:").split())
a=[]
s=""
while n==0 or m==0:
    break
for i in range(1,n+1):
    one=map(int,input("輸入矩陣數值第"+str(i)+"列為:").split())
    b=list(one)
    for j in range(m):
        c=b[j]
        a.append(c)
for i in range(m):
    for j in range(n):
        s=s+" "+str(a[j*m+i])    
    print("輸出矩陣數值第%d列為:%s"%((i+1),s))
    s=""      
