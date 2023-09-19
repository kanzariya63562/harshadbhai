#include<stdio.h>

int main()
{
   
    int choice, num, i;
    unsigned long int fact;

    while(1)
    {	printf("Main Menu\n");
        printf("\t1. Equality \n");
        printf("\t2. String Copy\n");
        printf("\t3. Concat\n");
        printf("\t4. Show\n");
        printf("\t5. Reverse\n ");
        printf("\t6. Palindrome\n");
        printf("\t7. Sub String \n");
        printf("\t8. Exit \n");
        printf("Please Enter your choice  :  \n");
        printf("Please Enter the string :\t Welcome  ");
        scanf("%d",&choice);
        
        
        
        
        
        	  char str[40];  
    printf (" \n Enter a string to be reversed:  ");  
    scanf ("%s", str);  
      
     
    printf (" \n After the reverse of a string: %s\t ", strrev(str));  
    
    
    
    
    
    
    char name1[20]; 
    char name2[20]; 
        
        
		
		
		
		
		
		switch(choice)
        {
            case 1:
                printf("Enter number:\n");
                scanf("%d", &num);
                fact = 1;
                for(i = 1; i <= num; i++)
                {
                    fact = fact*i;
                }
                printf("\n\nFactorial value of %d is = %lu\n\n\n",num,fact);
                break;
        
            case 2:
                printf("Enter number:\n");
                scanf("%d", &num);
                if(num == 1)
                printf("\n1 is neither prime nor composite\n\n");
                for(i = 2; i < num; i++)
                {
                    if(num%i == 0)
                    {
                        printf("\n%d is not a prime number\n\n", num);
                        break;
                    }
                
                }
                
                    
                    
                
                if(i == num) 
                {
                    printf("\n\n%d is a Prime number\n\n", num);
                    break;
                }
        
            case 3:
                printf("Enter number:\n");
                scanf("%d", &num);
        
                if(num%2 == 0) 
                    printf("\n\n%d is an Even number\n\n",num);
                else
                    printf("\n\n%d is an Odd number\n\n",num);
                break;
        
            case 4:
                printf("\n\n\t\t\tCoding is Fun !\n\n\n");
                exit(0);    
        }
    }
    printf("\n\n\t\t\tCoding is Fun !\n\n\n");
    return 0;
}