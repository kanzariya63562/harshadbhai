#include<stdio.h>

void main()
{
	int a=10;
	int b=20;
	printf("\na=%d,b=%d",a,b);
	if(a&&b)
	{
	
		printf("\nLine 1 is True");
	
	}
	else
	{
		printf("\nLine 2 is false");
		
	}
	b=10,a=10;
	if(a||b)
	{
		printf("\nLine 3 is true");
		
	}
	else
	{
		printf("\nLine 4 is false ");
	}
	
	
}