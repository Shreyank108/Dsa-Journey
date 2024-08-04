#linear Search   
# l=[1,2,3,7,6,5] 
# n=int(input()) 
# flag = 0
# for i in l: 
#     if i == n: 
#         flag=1    
#         break             
#     else :  
#         flag=0 

# if flag ==1 : 
#     print(True) 
# else : 
#     print (False ) 

#binary search   
# def binary_search(l,n): 
#     s=0   
#     e=len(l)-1   
#     while (s<e): 
#         mid =(s+e)//2   
#         if l[mid] == n: 
#             return mid   
#         elif l[mid]> n: 
#             e=mid-1   
#         elif l[mid]<n: 
#             s= mid + 1   
#     return -1   

# l=[1,2,3,4,5,6] 
# n=int(input("enter which element u want to find ")) 
# print(binary_search(l,n))
    