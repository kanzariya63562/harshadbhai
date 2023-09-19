#include<stdio.h>

void main()

{
	int a,b,choice;
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 choice calculator \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	printf("\n\n\t\tEnter a :");
	scanf("%d",&a);
	printf("\t\tEnter B :");
	scanf("%d",&b);
	printf("\n\t\tA = %d, B = %d",a,b);
	printf("\n\t\t====================");
	printf("\n\t\tPress 1. for addition");
	printf("\n\t\tPress 2. for subtraction");
	printf("\n\t\tPress 3. for maltiplaction");
	printf("\n\t\tPress 4. for division");
	printf("\n\t\t====================");
	printf("\n\t\tEnter your choice ?");
	scanf("%d",&choice);
	
	if(choice==1)
	{
		printf("\n\t\tAddition : %d",(a+b));
	}
   else	if(choice==2)
	{
		printf("\n\tSubtraction : %d",(a-b));
	}
	else if(choice==3)
	{
		printf("\n\tmultiplaction : %d",(a*b));
	}
	else if(choice==4)
	{
		printf("\n\tDivision : %d",((float)a/b));
	}
	else
	{
		printf("\tInvalide choice");
	}
	
	
	
	
}