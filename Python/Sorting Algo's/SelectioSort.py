l=[40,20,30,10,60,50]  
for i in range (len(l)): 
    for j in range(i+1): 
        if l[i]< l[j]: 
            l[i],l[j] = l[j],l[i]
print(l)