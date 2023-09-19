#include<stdio.h>  

	//WAP to find number is even or odd using ternary operator. 
  
int main()  
{  
    int n;  
  
    printf("Enter an integer number\n");  
    scanf("%d", &n);  
  
    (n % 2 == 0) ?  
    (printf("%d is Even number\n", n)) :  
    (printf("%d is Odd  number\n", n));  
  
    return 0;  
}  