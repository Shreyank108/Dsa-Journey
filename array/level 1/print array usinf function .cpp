using namespace std; 
#include <iostream> 

int krbhido(int arr[], int n){ 
    for (int i =0;i<n;i++)
    { 
        cout <<arr[i]<<" ";
    }
}
int main(){ 
    int n =5; 
    int arr[n]; 
    for (int i =0;i<n;i++){ 
        cin>>arr[i];
    }
    cout<<krbhido(arr,n);
}