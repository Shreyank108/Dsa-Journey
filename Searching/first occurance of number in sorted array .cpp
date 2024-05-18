// [10,20,30,30,30,30,40,50] 
using namespace std ;
#include <iostream> 
int binary_find(int arr[], int n, int target){ 
    int s =0; 
    int e= n-1; 
    int ans =-1;
    while (s<=e){ 
        int mid = (s+e)/2; 
        if (arr[mid]==target) {
            ans= mid; 
            e=mid-1 ;
        }
        else if (arr[mid]< target) 
          s=mid+1; 
        else   
           e=mid -1 ; 
    }
    return ans;
}
int main()
{ 
    int arr[]={10,20,30,30,30,30,40,50}; 
    int n = 8; 
    int target = 30; 
    cout <<"index of target element"<<binary_find(arr,n,target);
}