l=[1,2,6,5,4,3,6]  
a=1 
n=len(l) 
while a<n: 
    for i in range(n): 
        for j in range(i+1,n-a): 
            if (l[j]>l[j+1]): 
                l[j],l[j+1]=l[j+1],l[j] 
    a+=1   
print(l)