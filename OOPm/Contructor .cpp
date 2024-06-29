
 /**
 constructor is a function which automatically calls whwnever a object created     
types   
1. Default  
2. Parameterized  
3. copyied 
 **/ 

// using namespace std ;
// #include <iostream> 
// class A{ 
//     int a,b;
//     public: 
//        A() // default 
//        { 
//            a=10; b=20;
//            cout <<a<<b; 
//        } 
// }; 
// int main()
// { 
//      A obj ; 
// }

// using namespace std ;
// #include <iostream> 
// class A{ 
//     public: 
//        A(int a, int b) // Parameterized
//        { 
        
//            cout <<a<<b; 
//        } 
// }; 
// int main()
// { 
//     //  A obj= A(10,30) ;  
//     // or  
//     A obj(10,50);
// } 

using namespace std ;
#include <iostream> 
class A{ 
  int x,y; 
    public:
  A(int a,int b){  
    x=a; 
    y=b;
    cout <<x<<" "<<y;
  } 
  A(A &ref){ 
    x=ref.x; 
    y=ref.y; 
    cout <<x<<"  "<<y; 
  }
}; 
int main()
{ 
     A obj(10,20); 
     A obj2=obj; 

}