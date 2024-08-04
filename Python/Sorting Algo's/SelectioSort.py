l=[1,43,2,5,4,34,7] 
for i in range(len(l)): 
    for j in range(i+1): 
        if l[i]<l[j]: 
            l[i],l[j]=l[j],l[i] 
print(l)