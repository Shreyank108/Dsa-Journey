def MergeSort(arr): 
    if len(arr)>1  : 
        #Divide        
        mid = len(arr)//2   
        left = arr[:mid] 
        right = arr[mid:] 
        
        #conquer   
        MergeSort(left) 
        MergeSort(right) 
        
        #merge   
        i=j=k =0    
        
        while i<len(left) and j < len(right):    
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1   
            else : 
                arr[k]= right[j]  
                j+=1 
            k+=1   
        
        while i<len(left): 
            arr[k]= left[i] 
            i+=1 
            k+=1  
        while j< len(right): 
            arr[k] = right[j] 
            j+=1 
            k+=1 
        
l=[20,50,30,60,10,40,70] 
MergeSort(l) 
print(l) 