one=int(input(""))
a=120*2.10
b1,b2=210*3.02,210*2.68
c1,c2=170*4.39,170*3.61
d1,d2=200*4.97,200*4.01
e1,e2=(one-700)*5.63,(one-700)*4.50
if one<=120:
    print("summer months:%0.2f"%(one*2.10))
    print("non-summer months:%0.2f"%(one*2.10))
elif 330>=one>120:
    print("summer months:%0.2f"%((one-120)*3.02+a))
    print("non-summer months:%0.2f"%((one-120)*2.68+a))
elif 500>=one>330:
    print("summer months:%0.2f"%((one-330)*4.09+a+b1))
    print("non-summer months:%0.2f"%((one-330)*3.61+a+b2))
elif 700>=one>500:
    print("summer months:%0.2f"%((one-500)*4.97+a+b1+c1))
    print("non-summer months:%0.2f"%((one-500)*4.01+a+b2+c2))
else:
    print("summer months:%0.2f"%(e1+a+b1+c1+d1))
    print("non-summer months:%0.2f"%(e2+a+b2+c2+d2))
    

