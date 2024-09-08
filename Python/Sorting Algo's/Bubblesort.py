'''
  Bubble Sort     
        Complexity : O(n) 
        Space Complexity : O(1) 
        
'''

l=[10,60,20,40,30,50] 
a=1   
while a < len(l):    
    for i in range (len(l)-a): 
        if l[i+1] < l[i]: 
            l[i],l[i+1] =l[i+1],l[i]
    a+=1   
print(l)