using namespace std ;
#include <iostream>
int count =0;
class A{
    public: 
    A()
    { 
        cout <<"object "<<++count<<" created"<<endl;
    } 
    ~A()
    { 
        cout <<"object "<<count--<<" dealocated"<<endl;
    }

}; 
int main()
{ 
    A obj,obj2,obj3; 
}