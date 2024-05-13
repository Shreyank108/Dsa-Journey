using namespace std ;
#include <iostream> 
int getans(int arr[] , int n){ 
    int ans = 0;
    for (int i =0;i<n;i++)
    { 
             ans = ans^arr[i]; 
    }
    return ans ;
}
int main()
{ 
    int arr[]={1,2,3,2,1,3,6}; 
    int n =7; 
    cout <<"The final answer is " <<getans(arr,n);
}