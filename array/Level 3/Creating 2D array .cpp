using namespace std ;
#include <iostream> 
int main()
{ 
    int n =3; 
    int arr[n][n]; 
    for (int i =0;i<n;i++)
    { 
        for (int j =0;j<n;j++)
        { 
            cin>>arr[i][j];
        }
    }
    for (int i =0;i<n;i++)
    { 
        for (int j =0;j<n;j++)
        { 
            cout <<arr[i][j]<<" ";
        }
        cout <<endl;
    }
}