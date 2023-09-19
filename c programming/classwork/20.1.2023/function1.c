#include<stdio.h>
void f1()
{
	printf("\nFunction Called.");
}

void f2()
{
	printf("\nFuction Called.");
}
void main()

{
	printf("\nBefore Function Called.");
	f1(); //Fuction Utilization.
	f2();
	printf("\nAfter Fuctoin Called.");
}