using namespace std ;
#include <iostream> 
int main()
{ 
    int arr[][3]={
        {1,2,3},
        {4,5,6},
        {7,8,9}
    }; 
    bool flag ;
    int n =3;
    int target = 10;
    for (int i =0;i<n;i++)
    {
         for (int j =0;j<n;j++)
         { 
                 if ( arr[i][j] == target){
                        flag =true; 
                 } 
         }
    }
    cout <<flag; 
}