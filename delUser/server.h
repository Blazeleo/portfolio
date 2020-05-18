#ifndef DEL_H
#define DEL_H

#define BUFFER_SIZE 1000
#define MAX 256

FILE *File1, *File2;
int del, line, col;
char *word;

void FileDel(char *path);
int indexOf(FILE *fptr, const char *word, int *line, int *col);
#endif
