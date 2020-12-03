#include <stdio.h>
#include <stdlib.h>

typedef struct password_validator {
	unsigned short min_count;
	unsigned short max_count;
	char target_char;
	char password[20];
} password_validator;

int main() {
	FILE * fp;
	int c;

	fp = fopen("input.txt", "r");
	fprintf(fscanf(fp, "%s"));
	fclose(fp);
	return(0);

}
