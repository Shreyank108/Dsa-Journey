using namespace std ;
#include <iostream> 
class Bank{ 
    private : 
       int pin, amount; 
    public: 
       string name , bankName; 
       int accNumber,IFSC; 
    void input(){ 
         pin=1234; 
         amount = 69000; 
         name="Shreyank"; 
         bankName="PayTm"; 
         accNumber =12345678; 
         IFSC =23948;
    }
    void show()
    {
         cout <<"pin"<<pin<<endl;
         cout <<"amount"<<amount<<endl;
         cout <<"name"<<name<<endl;
         cout <<"banName"<<bankName<<endl;
         cout <<"accNumber"<<accNumber<<endl;
         cout <<"IFSC"<<IFSC<<endl;
    }
};
int main(){
   
   Bank a; 
   a.show(); 

   cout <<"Raj want to acess this "; 
   cout<<a.pin<<endl;
   cout <<a.amount<<endl; 
   cout <<a.name<<endl; 
   cout <<a.bankname<<endl; 
   cout <<a.accNumber<<endl; 
   cout <<a.IFSC<<endl;

}
