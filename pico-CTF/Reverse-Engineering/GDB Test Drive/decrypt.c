#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* rotate_encrypt(char* encrypted_text)
{
	char* copy = strdup(encrypted_text);
  	size_t length = strlen(copy);
  	size_t i;
  	for(i = 0; i < length; i++)
 	{
     		if(copy[i] > 0x20)
     		{
       			if(copy[i] != 0x7F)
       			{
          			int no_name = copy[i] + 0x2F;
          			if(no_name > 0x7E)
          			{
                			copy[i] = (no_name) - 0x5E;
           			}
           			else
          			{
              				copy[i] = (no_name);
          			}
       			}
     		}
	}
    	return copy;
}



int main()
{
	char encrypted_text[32];
	printf("Enter the encrypted_text: ");
	scanf("%s",encrypted_text);
	char* flag = rotate_encrypt(encrypted_text);
	printf("Flag:%s\n",flag);
	free(flag);
	return 0;
}
