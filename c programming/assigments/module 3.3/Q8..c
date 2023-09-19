#include <stdio.h>
#include <stdlib.h>

		//Write a program of structure employee that provides the followinginformation -print and display empno, empname, address and age.
 
typedef struct{
    char name[30];
    int id;
    double salary;
} Employee;
 
int main()
{
    
    int n=2;

    
    Employee employees[n];
 
   t
    printf("Enter %d Employee Details \n \n",n);
    for(int i=0; i<n; i++){
        printf("Employee %d:- \n",i+1);

       
        printf("Name: ");
        scanf("%[^\n]s",employees[i].name);

        
        printf("Id: ");
        scanf("%d",&employees[i].id);

       
        printf("Salary: ");
        scanf("%lf",&employees[i].salary);

        
        char ch = getchar();
 
        printf("\n");
    }
 
    
    printf("-------------- All Employees Details ---------------\n");
    for(int i=0; i<n; i++){
        printf("Name \t: ");
        printf("%s \n",employees[i].name);
 
        printf("Id \t: ");
        printf("%d \n",employees[i].id);
 
        printf("Salary \t: ");
        printf("%.2lf \n",employees[i].salary);
 
        printf("\n");
    }
 
    return 0;
}