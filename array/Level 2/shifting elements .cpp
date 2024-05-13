#include <iostream> 

using namespace std;

int main()
{ 
    int arr[] = {10, 20, 30, 40, 50, 60}; 
    int n = sizeof(arr) / sizeof(arr[0]);
    int temp = arr[n - 1];  
    int k; 
    cout << "Enter number of times to rotate: "; 
    cin >> k; 

    for (int j = 0; j < k; j++) 
    { 
        for (int i = n - 1; i > 0; i--)
        { 
            arr[i] = arr[i - 1];
        } 
        arr[0] = temp;
        temp = arr[n - 1]; 
    }

    for (int i = 0; i < n; i++)
    { 
        cout << arr[i] << " ";
    }
    
    return 0;
}
