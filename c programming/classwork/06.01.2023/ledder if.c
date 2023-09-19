#include<stdio.h>
/*15.Write a program user enter the 5 subjects mark. You have to make a totaland find the percentage.
Percentage > 75 you have to print“Distinction”
Percentage > 60 and percentage <= 75 you have to print “Firstclass”
Percentage >50 and percentage <= 60 you have to print “Second class” Percentage > 35 and
percentage <= 50 you have to print “Pass class” Otherwise print“Fail”*/

void main()
{
	int rollno,s1,s2,s3,s4,s5,total;
	char name[20];
	float per;
	printf("\nEnter roll.no :");
	scanf("%d",&rollno);
	fflush(stdin);
	printf("\nEnter name :");
	//scanf("%s",&name);
	gets(name);
	printf("\nEnter physics marks :");
	scanf("%d",&s1);
	printf("\nEnter chemistry marks :");
	scanf("%d",&s2);
	printf("\nEnter math marks :");
	scanf("%d",&s3);
	printf("\nEnter account marks :");
	scanf("%d",&s4);
	printf("\nEnter english marks :");
	scanf("%d",&s5);
	printf("\nRoll No. %d",rollno);
	printf("\nname: %s",name);
	
	total=s1+s2+s3+s4+s5;
	per=(float)total/5;
	printf("\nTotal:%d",total);
	printf("\nPercentage : %.2f",per);
	printf("\nClass :");
	
	if(per>=75)
	{
		printf("distinction");
	}
	else if(per>=60)
	{
        printf("first class");	
	}
	else if(per>=50)
	{
		printf("second class");
	}
	else if(per>=40)
	{
		printf("pass");
	}
	else
	{
		printf("fail!!");
	}
	
	
}