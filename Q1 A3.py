a=input()
b=set(a)

b=list(b)

lst=[]
for i in range (0,len(a)):
    c=0
    
    d=a[i]
    
    if d not in lst:      
        for j in range (0,len(a)):
            if d==a[j]:
                c=1+c
        print('number of times',a[i],'has appeared is',c)
    lst.append(d)
    
    
