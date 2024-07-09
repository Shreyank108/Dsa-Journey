using namespace std ;
#include <iostream> 
class A{ 
      
      public : 
      void person()
      { 
        cout <<"Good Morning "<<endl;
      }

} ; 
 
class B: public A { 
    public :
     void person()
      { 
        cout <<"Good Night  "<<endl;
      }
};
int main()
{  
    B p; 
    p.person();  
    p.A::person(); 
    return 0; 
}