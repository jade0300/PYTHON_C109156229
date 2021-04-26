one=map(int,input("輸入一整數序列為：").split())
tt=list(one)
c=len(tt)/2
b=[]
for i in tt:
    b.append(tt.count(i))
d=max(b)
f=b.index(d)
if d>c:
    print("過羊元素:%d"%tt[f])
else:
    print("過羊元素:NO")
    