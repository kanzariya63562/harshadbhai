#include<stdio.h>

void main()
{
	int age;
	printf("\nEnter your Age : ");
	scanf("%d",&age);
	
	if(age>=18)
	{
		printf("\nYou are  Eligible to vote.");
	}
	else
	{
		printf("\nYou are not Eligible to Vote.");
	}
}