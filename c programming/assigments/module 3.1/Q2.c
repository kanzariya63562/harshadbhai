#include<stdio.h>

void main()

{
	//Write a program to make Simple calculator (to make addition, subtraction,
	//multiplication, division and modulo) 
	
		int num1,num2;
	printf("\nEnter number 1 :");
	scanf("%d",&num1);
	printf("\nEnter number 2 : ");
	scanf("%d",&num2);
	
	printf("\nNumber1 = %d \nNumber2 = %d",num1,num2);
	printf("\nAddition : %d",(num1+num2));
	printf("\nSubtraction : %d",(num1-num2));
	printf("\nMultiplication : %d",(num1*num2));
	printf("\nDivision : %.2f",(float)num1/num2);

}