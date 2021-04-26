one=input("請輸入正整數:")
g=[]
s=[]
for i in range(0,len(one)+1):
    for j in range(i+1,len(one)+1):       
        g.append(one[i:j])
def one1(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True  
for i in range(0,len(g)):
    if one1(int(g[i]))==True:
        s.append(int(g[i]))    
if s!=[]: 
    print("子字串中最大的質數值為:",max(s))
else:
    print("子字串中最大的質數值為:","No prime found")
               
          
            
         