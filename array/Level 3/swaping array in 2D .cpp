using namespace std ;
#include <iostream> 
int main()
{ 
    int arr[][3]={
        {1,2,3},
        {4,5,6},
        {7,8,9}
    }; 
    int n=3;
        for (int i =0;i<n;i++)
    { 
        for (int j =0;j<n;j++)
        { 
            cout <<arr[i][j]<<" ";
        }
        cout <<endl;
    }


    for (int i =0;i<n;i++)
    { 
        for (int j =i+1 ;j<n;j++)
        {
             swap(arr[i][j] , arr[j][i]);
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