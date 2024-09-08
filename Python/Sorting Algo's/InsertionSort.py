''' 
 Insertion Sort    
 
    Time Complexity 
      
        Best Case -   
            Already Sorted Array 
            element - n    
            comparision - n-1   
            swap -0 
            complexity - O(n) 
            
        Worst Case -    
            Reverse Sorted array   
            element -n   
            comparision - n -1    
            swap - n-1   
            complexity - O(n^2)
''' 

l=[40,60,50,10,30,20] 
for i in range(1,len(l)): 
    current =l[i] 
    j = i-1     
    while j>=0 and l[j] > current : 
        l[j+1]= l[j]
        j-=1    
    l[j+1] = current    
print(l)