#include<stdio.h>

void main()
	
	//forloop

{
	int i,n;
	printf("Enter number");
	scanf("%d",&n);
	
	for(i=1;i<=10;i++)
	{
	
		printf("%dx%d=%d\n",n,i,(n*i));
	}
}