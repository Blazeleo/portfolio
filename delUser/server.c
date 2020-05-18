#include<stdio.h>
#include"server.h"

#include <string.h>
#include <stdlib.h>

/**
 * Finds, first index of a word in given file. First index is represented
 * using line and column.
 */

int indexOf(FILE *fptr, const char *word, int *line, int *col)
{
    char str[BUFFER_SIZE];
    char *pos;

    *line = -1;
    *col  = -1; 

    while ((fgets(str, BUFFER_SIZE, fptr)) != NULL)
    {
        *line += 1;

        // Find first occurrence of word in str
        pos = strstr(str, word);

        if (pos != NULL)
        {
            // First index of word in str is 
            // Memory address of pos - memory
            // address of str.
            *col = (pos - str);
            break;
        }
    }


    // If word is not found then set line to -1
    if (*col == -1)
        *line = -1;

    return *line;
	fclose(fptr);
}

void FileDel(char *path){
	
	FILE *fptr = fopen(path, "r");
	indexOf(fptr, word, &line, &col);

	if (!fptr)
    {
        printf("Unable to open file.\n");
        printf("Please check you have read/write previleges.\n");

        exit(EXIT_FAILURE);
    }

    if (line != -1)
	{
		del=line+1;
	}

	else{
		printf("Word not found, try again\n");	
		exit(1);
	}
	
    printf("'%s' found at line: %d, col: %d\n", word, line + 1, col + 1);

    int lno = del, ctr = 0;
    char ch, cha;
    FILE *fptr2;
	char *fname = path;
    char str[MAX], temp[] = "temp.txt";
    
	fname = path;
    fptr2 = fopen(temp, "w"); // open the temporary file in write mode 
    if (!fptr2) 
	{
        printf("Unable to open a temporary file to write!!\n");
        fclose(fptr);
        return;
    }
    
	rewind(fptr);

    // copy all contents to the temporary file except the specific line
    while (!feof(fptr)) 
    {
        strcpy(str, "\0");
        fgets(str, MAX, fptr);
        if (!feof(fptr)) 
        {
            ctr++;
            /* skip the line at given line number */
            if (ctr != (line+1)) 
            {
                fprintf(fptr2, "%s", str);
		
            }
        }
    }

    fclose(fptr);
	fclose(fptr2);

	fptr = fopen(fname, "w");
	fptr2 = fopen(temp, "r"); 
	
	while((cha = fgetc(fptr2)) != EOF)
    	fputc(cha, fptr);

    remove(temp);  		// remove the original file 
    fclose(fptr2);
	fclose(fptr);
    //rename(temp, fname); 	// rename the temporary file to original name
//------ Read the file ----------------/
            fptr=fopen(fname,"r"); 
            ch=fgetc(fptr); 
            printf(" \nNow the content of the file %s is : \n",fname); 
            while(ch!=EOF) 
            { 
                printf("%c",ch); 
                 ch=fgetc(fptr); 
            }
            fclose(fptr);
//------- End of reading ---------------/
    return;
}

