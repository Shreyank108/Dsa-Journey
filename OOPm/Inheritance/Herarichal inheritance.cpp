using namespace std ;
#include <iostream>
class engine {
    protected:
    string integration; 
    public:
    void system(){ 
       integration = "'s engine has been setup";
    }
    void show ()
    { 
        cout <<integration; 
    }
}; 

class Car :public engine{
    public:
    void car_engine()
    { 
        cout <<"car"<<integration<<endl; 
    }
};

class Aeroplane : public engine{ 
    public:
        void aero_engine(){ 
            cout <<"aerophane"<<integration;
        }
};
int main()
{ 
     Car p; 
     p.system(); 
     p.car_engine(); 

     Aeroplane m; 
     m.system(); 
     m.aero_engine(); 
}