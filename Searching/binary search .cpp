using namespace std ;
#include <iostream> 
int binary(int arr[], int n, int p){ 
    int start = 0; 
    int end = n-1 ; 
    while (start < end){ 
        int mid = (start+end)/2; 
        if (arr[mid] == p)
        { 
            return mid ; 
        }
        else if (arr[mid]<p) 
                   start=mid+1 ;
        else   
           end=mid-1  ;
    }
    return -1 ;
}
int main()
{ 
    int arr[]={1,2,3,4,5}; 
    int n =sizeof(arr)/sizeof(int);  
    int p = 3; 
    cout <<binary(arr,n,p); 
}