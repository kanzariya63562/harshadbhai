#include<stdio.h>

void main()
{
	int a,b;
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter B : ");
	scanf("%d",&b);
	printf("A = &d B = &d",a,b);
	
	if(a>0)
	{
		printf("\n%d is positive value",a);
	}
	else
	{
		printf("\n%d is negative value",a);
	}
	
	printf("\nOutside if block");
	
}