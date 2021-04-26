tt=[]
tt=eval(input("輸入值為:"))
one=list(tt)
a=len(one)
one.sort()
two=""
for i in range(a):
    two += str(one[i])
one.reverse()
yy=""
for i in range(a):
    yy+=str(one[i])
print("最大值數列與最小值數列差值為:%d"%(int(yy)-int(two)))