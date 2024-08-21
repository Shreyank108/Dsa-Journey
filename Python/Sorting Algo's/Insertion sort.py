l=[6,4,3,5,2] 
for i in range(1,len(l)): 
    current = l[i] 
    j=i-1   
    while j>=0 and l[j]>current: 
        l[j+1]=l[j] 
        j-=1   
    l[j+1]=current
print(l)