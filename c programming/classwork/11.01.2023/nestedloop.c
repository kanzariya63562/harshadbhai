#include<stdio.h>

void main()

{
	int i,j;
	printf("Enter the value :");
	scanf("%d",&i);
	for(i=2;i<=7;i++)
	{
		for(j=1;j<=10;j++)
		{
			printf("%d x %d = %d\n",i,j,(i*j));
		}
	}
}