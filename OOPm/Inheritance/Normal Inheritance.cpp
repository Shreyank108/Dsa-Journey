// using property of one class into other class  
/* 
 Normal inheritance  
 Multilevel inheritance  
 Multiple inheretance 
 Herarical inheritance 
 */

using namespace std ;
#include <iostream>
class Dad{ 
    protected:
    int amount ; 
    public : 
    void assignation(){ 
        amount =5000; 
    }
};  
class Son : public Dad { 
     int money = 500; 
     public : 
     void Left_amount()
     { 
        cout<<money<<endl; 
        cout<<amount <<endl ; 
        cout <<"total amount after taken money from amount "<<"Rs. "<<amount -money<<endl; 
     }
};
int main()
{
     Son a;
     a.assignation(); 
     a.Left_amount(); 
     return 0; 
}