a=int(input("請輸入陣列大小:"))
s=[]
d=[]
z=""
for i in range(a):
    one=map(int,input("").split())
    one=list(one)
    for i in range(len(one)):
        s.append(one[i])
        d.append(one[i])
s.sort()
s.reverse()
print("最大值為:%d"%(s[0]+s[1]+s[2]))    
for i in range(3):
    q=d.index(s[i])
    if (q+1)%a!=0: 
        z+="("+str(q//a+1)+","+str((q+1)%a)+")"
    else:
        z+="("+str(q//a+1)+","+str(a)+")"
 
print("位置為%s"%z)     
