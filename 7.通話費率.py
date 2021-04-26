one,two=eval(input("輸入月租費形式及通話時間為:"))
if one==186:
    if 0<two*0.09-186<=186:
        print("通話費為:%d"%round(two*0.09*0.9))
    elif two*0.09-186>186:
        print("通話費為:%d"%round(two*0.09*0.8))
    else:
        print("通話費為:%d"%round(two*0.09))
elif one==386:
    if 0<two*0.08-386<=386:
        print("通話費為:%d"%round(two*0.08*0.8))
    elif two*0.08-386>386:
        print("通話費為:%d"%round(two*0.08*0.7))
    else:
        print("通話費為:%d"%round(two*0.08))
elif one==586:
    if 0<two*0.07-586<=586:
        print("通話費為:%d"%round(two*0.07*0.7))
    elif two*0.07-586>586:
        print("通話費為:%d"%round(two*0.07*0.6))
    else:
        print("通話費為:%d"%round(two*0.07))
elif one==986:
    if 0<two*0.06-986<=986:
        print("通話費為:%d"%round(two*0.06*0.6))
    elif two*0.06-986>986:
        print("通話費為:%d"%round(two*0.06*0.5))
    else:
        print("通話費為:%d"%round(two*0.06))


