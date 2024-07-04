// Encapsulation is a concept of OOp where , it wrap the data member and Member Function into a single unit  
// Used to secure 100% data 
// always privzate the data member  , public your member functiuon  

#include<iostream>
using namespace std;
class theif { 
    string name , adress ; 
    int mob; 
    public: 
    void input()
    { 
        name ="Raj"; 
        adress="Karoad" ;
        mob=1234567891;
    } 
    void acess()
    { 
        cout <<name<<endl<<adress<<endl<<mob;
    }
};
class police : public theif { };
int main()
{ 
    police o; 
    o.input(); 
    o.acess(); 
}