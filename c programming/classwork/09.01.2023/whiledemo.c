#include<stdio.h>
/*

1) while loop :

	syntax :
			initialization;
			
			while(condition)
			{
				statement;
				updation;
			}
			
	- While loop is called as Entry Controlled Loop.
	  Because the condition is checked first and then the block 
	 is executed.
	-No Semicolon after condition.

*/

void main()
{
	int i=1;  // Initialization.
	
	while(i<=10) // Condition
	{
		printf(" %d. = %d\n",i,(i)); // statement
		i++;
	}
}











