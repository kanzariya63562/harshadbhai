#include<stdio.h>

	//WAP to make simple calculator (operation include Addition, Subtraction,Multiplication, Division, modulo) 

void main ()

{
	int num1 = 4;
	int num2 = 2;
	printf("Enter Number1 = %d \nEnter Number2 = %d",num1,num2);
	printf("\nAddition : %d",(num1+num2));
	printf("\nSubtraction : %d",(num1-num2));
	printf("\nMultiplication : %d",(num1*num2));
	printf("\nDivision : %.2f ",(float)num1/num2);
	printf("\nmodulo %d",(num1%num2));
}