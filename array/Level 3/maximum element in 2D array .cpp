using namespace std ;
#include <iostream> 
#include <limits.h>
int main()
{ 
    int arr[][3]={
        {1,2,3},
        {4,55,6},
        {7,8,9}
    }; 
    int n = 3;
    int max_ans = INT_MIN;
    for (int i =0;i<n;i++)
    {
         for (int j =0;j<n;j++)
         { 
                if (arr[i][j] > max_ans)
                { 
                    max_ans= arr[i][j];
                }
         }
    }
    cout <<max_ans; 
    
}