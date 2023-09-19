#include<stdio.h>
void f1()
{
	f2();
	printf("\nFunction1 Called.");
}

void f2()
{
	printf("\nFuction2 Called.");
}
void main()

{
	printf("\nStart Function.");
	f1(); //Fuction Utilization.
	f2();
	printf("\nEnd Fuctoin.");
}