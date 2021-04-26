a=[['123', '456', '789', '321', '654'], ['Tom', 'Cat', 'Nana', 'Lim', 'Won'], ['DTGD', 'CSIE', 'ASIE', 'DBA', 'FDD']]
one=input("輸入查詢學號為:")
for i in range(5):
    if a[0][i]==one:
        print("學生資料為:%s %s %s"%(a[0][i],a[1][i],a[2][i]))