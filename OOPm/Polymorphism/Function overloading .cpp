using namespace std ;
#include <iostream> 

class A{
    int num1 ,num2,num3; 
    public : 
    void samu()
    { 
        cout <<"Enter a num", 
        cin>>num1>>num2; 
        num3 = num1+ num2 ; 
        cout <<"Sum "<<num3<<endl; 
    }
    void samu(int a,int b)
    { 
        cout <<"Multi "<<a*b; 
    }
};
int main()
{ 
    A p; 
    p.samu(4,5); 
    p.samu();
    return 0; 
}