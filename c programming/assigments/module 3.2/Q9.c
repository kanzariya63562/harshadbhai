#include <stdio.h>

		//Write a program to find out the max from given number (E.g., No: -1562Max number is 6). 

int main()
{
    int num1, num2;

   
    printf("Enter two numbers: ");
    scanf("%d%d", &num1, &num2);

    
    if(num1 > num2)
    {
        printf("%d is maximum", num1);        
    }

   
    if(num2 > num1)
    {
        printf("%d is maximum", num2);
    }

   
    if(num1 == num2)
    {
        printf("Both are equal");
    }

    return 0;
}