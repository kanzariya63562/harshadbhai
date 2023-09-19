#include<stdio.h>

int main()

{
	  char str[40]; 
    printf (" \n Enter a string to be reversed: ");  
    scanf ("%s", str);  
      
      
    printf (" \n After the reverse of a string: %s ", strrev(str));  
    
    
    
    
    
    
    char name1[20]; 
    char name2[20]; 
    
    int i;  

    printf("Enter name1: ");  
    scanf("%s",name1);  
    printf("\nEnter name2: ");  
    scanf("%s",name2);  

    
    for(i=0;name1[i]!='\0';i++);   
        
    for(int j=0;name2[j]!='\0';j++)  
    {     
        name1[i]=name2[j];  
        i++;  
    } 

    
    name1[i]='\0';  
    printf("After concatenation is done, the new concatenated string will be: %s", name1);  
    
    
    
    
    
    
    int n, reversed = 0, remainder, original;
    printf("Enter an integer: ");
    scanf("%d", &n);
    original = n;

    
    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }


    if (original == reversed)
        printf("%d is a palindrome.", original);
    else
        printf("%d is not a palindrome.", original);






char str1[20] = "C programming";
  char str2[20];

  
  strcpy(str2, str1);

  puts(str2); 






char str[1000]; 
 
    
    printf("Enter the string: ");
    scanf("%s", str); 
    

    int length;
    
    
    length = strlen(str); 
    
    
    printf("The length of the string is %d", length); 
    
    
    
    
    
    
    
    char str[1000], ch;
    int count = 0;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    printf("Enter a character to find its frequency: ");
    scanf("%c", &ch);

    for (int i = 0; str[i] != '\0'; ++i) {
        if (ch == str[i])
            ++count;.*/
            
            
            
            
            
            
            
             char line[150];
  int vowels, consonant, digit, space;

  
  vowels = consonant = digit = space = 0;

  
  printf("Enter a line of string: ");
  fgets(line, sizeof(line), stdin);

  
  for (int i = 0; line[i] != '\0'; ++i) {

    line[i] = tolower(line[i]);
    

    
    if (line[i] == 'a' || line[i] == 'e' || line[i] == 'i' ||
        line[i] == 'o' || line[i] == 'u') {

      
      ++vowels;
    }

    
    else if ((line[i] >= 'a' && line[i] <= 'z')) {
      ++consonant;
    }

    
    else if (line[i] >= '0' && line[i] <= '9') {
      ++digit;
    }

    
    else if (line[i] == ' ') {
      ++space;
    }
  }

  printf("Vowels: %d", vowels);
  printf("\nConsonants: %d", consonant);
  printf("\nDigits: %d", digit);
  printf("\nWhite spaces: %d", space);









 

	char str[50]; 
	int len,i,spaces=0; 
	printf("Enter the String\n"); 
	gets(str); 
	len=strlen(str); 
	for(i=0;i<len;i++){ 
		if(str[i]==' ') 
			spaces++; 
	} 
	printf("Total spaces are : %d\n",spaces); 
 
 
  
    return 0;
}