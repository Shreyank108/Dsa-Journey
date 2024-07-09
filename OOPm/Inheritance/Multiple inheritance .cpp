using namespace std ;
#include <iostream>
class Engine{
    protected:
    string engine; 
    public: 
    void Engine_Establish();
    void Whats_about_engine();
}; 
void Engine :: Engine_Establish()
{ 
engine = "it is established already";
}
void Engine  :: Whats_about_engine()
{ 
    cout <<engine<<endl; 
}
class Roof{
    protected:
    string roof; 
    public :  
    void Roof_establishment()
    { 
        roof="Roof existed";
    }
    void Whats_about_roof()
    { 
        cout <<roof<<endl; 
    }
}; 

class Car: public Engine , public Roof{ 
    protected:
    string car; 
    public: 
    void car_establishment()
    { 
        car ="Car is baking "; 
    } 
    void Whats_about_car()
    { 
          cout <<car<<endl;
    }
};
int main()
{ 
      Car p; 
      p.Engine_Establish(); 
      p.Whats_about_engine(); 
      p.Roof_establishment(); 
      p.Whats_about_roof();  
      p.car_establishment(); 
      p.Whats_about_car(); 
}