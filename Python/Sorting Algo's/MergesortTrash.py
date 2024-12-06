# def merger(arr): 
#     if len(arr)> 1 : 
#         mid = len(arr)//2 
#         left = arr[:mid]  
#         right = arr[mid:] 
        
#         merger(left) 
#         merger(right)    
        
#         i=j=k=0 
        
#         while i<len(left) and j< len(right): 
#             if left[i] < right[j]: 
#                 arr[k] = left[i] 
#                 i+=1  
#             else : 
#                 arr[k]=right[j] 
#                 j+=1 
#             k+=1 
        
#         while i < len(left): 
#             arr[k]= left[i] 
#             i+=1 
#             k+=1 
        
#         while j<len(right): 
#             j+=1 
#             k+=1 
            
# l=[2,5,4,3,7,6,8] 
# merger(l) 
# print(l) 

# Quickl sort  

