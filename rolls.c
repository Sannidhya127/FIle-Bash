#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	char data[100] = "This is a sample program to be included in my file bash project folder";
	printf("%s\n", data);

	int num = 656;
	int *numptr = &num;

	printf("The number is: %d\n", num);
	printf("The pointer number is: %d\n", numptr);
	printf("The pointer value of the number is: %p\n", numptr);
	scanf("%d");
	return 0;
}