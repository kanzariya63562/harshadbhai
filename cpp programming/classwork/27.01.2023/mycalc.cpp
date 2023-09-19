#include<iostream>
using namespace std;

int main()
{
	int a,b,choice;
	cout<<"\n\n\t\t(((((((((()))))))))) Choice Calculator  (((((((((((((())))))))))";
	cout<<"\n\n\t\tEnter A : ";
	cin>>a;
	cout<<"\t\tEnter B : ";
	cin>>b;
		cout<<"\nvalue of A :"<<a;
	    cout<<"\nvalue of B :"<<b;
	cout<<"=================================";
	cout<<"\n\nPress 1. for Addition";    
    cout<<"\n\nPress 2. for Subtraction";
	cout<<"\n\nPress 3. for Multiplication";
	cout<<"\n\nPress 4. for Division";
	cout<<"\n\t\t=================================\n";
    cout<<"\n\t\tEnter your choice ? ";	
	cin>>choice;
	
	if(choice==1)
	{
		cout<<"\n Addition :"<<(a+b);
	}
	else if(choice==2)
	{
		cout<<"\n subtraction :"<<(a-b);
	}
	else if(choice==3)
	{
		cout<<"\n multiplication :"<<(a*b);
	}
	else if(choice==4)
	{
		cout<<"\n division :"<<((float)a/b);
	}
	else
	{
	    cout<<"\n\t\tInvalid Choice";
	}
	return 0;
}
	
