one1=input("輸入一字元為:")
one=list(one1)
a=len(one)
two=""
for i in range(a-1,-1,-1):
    two += one[i]
if one1==two:
    print("YES")
else:
    print("NO")