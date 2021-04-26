m=int(input("請輸入階層值M:"))
total=n=1
while(m>total):
    total*=n
    n+=1
print("超過M為%d的最小階層N值為:%d"%(m,n-1))
    
    
    