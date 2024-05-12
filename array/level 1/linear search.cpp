using namespace std ;
#include <iostream> 
int main()
{ 
      int n; 
      cin>>n; 
      int arr[n]; 
      for (int i =0;i<n;i++)
      { 
         cin>>arr[i]; 
      } 
      for (int i =0;i<n;i++)
      {
         cout<<arr[i];
      }
      int p; 
      bool flag ; 
      cout<<"finding elem"; 
      cin>>p; 
      for (int i =0;i<n;i++)
      { 
         if (arr[i]==p)
         { 
            flag =1;
            break; 
      }
      }
      if (flag ==1){ 
        cout <<"found"; 
      }

}