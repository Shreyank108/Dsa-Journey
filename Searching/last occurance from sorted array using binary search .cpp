using namespace std ;
#include <iostream> 
int binary(int arr[], int n , int p){ 
    int s=0 ; 
    int e= n-1; 
    int ans =-1 ;
    while (s<=e){ 
        int mid = s+(e-s)/2 ; 
        if (arr[mid] == p){ 
               ans = mid  ; 
               s=mid +1;
        } 
        else if ( arr[mid]<p){
             s=mid +1;
        } 
        else { 
            e= mid-1 ;
        }
    }
    return ans ;
}
int main()
{ 
    int arr[]={1,2,3,3,3,3,4,5}; 
    int n= sizeof(arr)/sizeof(int); 
    cout <<n;
    int target = 3; 
    cout <<binary(arr,n,target);   

}