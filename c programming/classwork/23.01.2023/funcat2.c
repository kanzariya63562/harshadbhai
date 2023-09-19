#include<stdio.h>

int add(int d,int g)

{
	printf("\nInside UFD A = %d, B = %d",d,g);
	return d+g;
	
}


void main()

{
	int a=13,b=42,sum;
	sum = add(a,b);
	printf("\nAddition : %d",sum);
	if(sum%2==0)
	{
		printf("\nsum is even");
	}
	else
	{
		printf("\nsum is odd");
	}
}