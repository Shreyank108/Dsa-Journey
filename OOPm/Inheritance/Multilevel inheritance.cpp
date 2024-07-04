using namespace std ;
#include <iostream>
class A{
    protected: 
    int a,b,c; 
    public: 
    void input()
    { 
        a=2; 
        b=4;
    }
    void Sum()
    { 
      c= a+b; 
       cout<<  c;

    }
}; 
class B: public A{ 
      protected : 
      int d; 
      public : 
      void multiply()
      { 
        d=c*2;
        cout<< d;
      }
};
class C : public B{ 
        protected : 
        int e; 
        public : 
        void divide()
        { 
            e=d/2; 
            cout<< e;
        }
};
int main()
{ 
     C coc; 
     coc.input(); 
     coc.Sum(); 
     coc.multiply() ;
     coc.divide();
}