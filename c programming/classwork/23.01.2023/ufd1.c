#include<stdio.h>

void add(int x,int y)
{
	printf("\nInside UFD X = %d, Y = %d",x,y);
	printf("\nAddition : %d",(x+y));
}

void main()
{
	int a,b;
	
	printf("\n Enter A = ");
	scanf("%d",&a);
	printf("\n Enter B = ");
	scanf("%d",&b);
	printf("\nStrat function");
	add(a,b);
	printf("\nstop function");
}