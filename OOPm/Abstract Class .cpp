/*
 Abstract class are such class that you are defined to inherit only by other classes .
 the purpose od abstract classes is to provide a stucture to other classes which you can inherit  

 A class which contain at least one pure virtual function called abstract class  

*/ 

using namespace std ;
#include <iostream>  
class animal { 
    virtual void sound()=0;
};
class dog: public animal{ 
    public : 
     void sound ()
     { 
        cout <<"whoof whoof..."; 
     }
};
int main()
{ 
        dog p; 
        p.sound();
}