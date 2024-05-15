using namespace std ;
#include <iostream>
#include <vector>  

void print(vector<int> v){ 

    for (int i =0;i<v.size();i++)
    { 
        cout <<v[i];
    }
}

int main()
{ 
   vector<int> v; 

   v.push_back(1);
   v.push_back(2);
   v.push_back(3);
   v.pop_back();
   v.push_back(5); 
   
   print(v);

}