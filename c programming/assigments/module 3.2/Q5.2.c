#include<stdio.h> 
#include<stdlib.h> 

	//Looping programs:2. WAP to take 10 no. Input from user and find out … .
 
int main() 
{ 
	int sum=0,num; 
	printf("Enter 10 numbers : "); 
	for(int i=0;i<10;i++) 
	{ 
		scanf("%d",&num); 
		sum+=num; 
	} 
	printf("Sum = %d",sum); 
} 
