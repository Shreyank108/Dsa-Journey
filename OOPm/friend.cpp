// friend Function is a function which is not the 
// member of class instead of that it can acess private and protected member of class  

using namespace std ;
#include <iostream> 
class shreyank{  
    private : 
     string tv ; 
    public : 
        void show(){ 
            tv="Watching Pokemon";
        } 
    friend void raj(shreyank r); 
};
void raj(shreyank r)
{ 
    cout<<"i'm also "<<r.tv; 
}
int main()
{ 
    shreyank a; 
    a.show();  
    raj(a); 
}