# l=[1,2,6,5,4,3,6]  
# a=1 
# n=len(l) 
# while a<n: 
#     for i in range(n): 
#         for j in range(i+1,n-a): 
#             if (l[j]>l[j+1]): 
#                 l[j],l[j+1]=l[j+1],l[j] 
#     a+=1   
# print(l) 

# l=[4,3,6,5,1,7,12,2] 
# a=1
# while a<len(l): 
#     for i in range(len(l)): 
#         for j in range(i+1,len(l)-a): 
#             if l[j]>l[j+1]: 
#                 l[j],l[j+1] = l[j+1],l[j] 
#     a+=1  
# print(l) 

l=[14,1,6,5,23,5,465,8] 
a=1  
while a<len(l): 
    for i in range(len(l)-a): 
        if l[i] > l[i+1]: 
            l[i],l[i+1]=l[i+1],l[i] 
    a+=1  
print(l)