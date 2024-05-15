#include <iostream>
using namespace std;

int binary(int arr[], int n, int key) {
    int s = 0;
    int e = n - 1;  

    while (s <= e) {
        int mid = s + (e - s) / 2;  

        if (arr[mid] == key) {
            return mid;
        } else if (arr[mid] < key) {
            s = mid + 1;  
        } else {
            e = mid - 1;  
        }
    }
    return -1;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);  
    int key = 5;

    int result = binary(arr, n, key);
    if (result != -1) {
        cout << "Element found at index: " << result << endl;
    } else {
        cout << "Element not found in the array." << endl;
    }

    return 0;
}
