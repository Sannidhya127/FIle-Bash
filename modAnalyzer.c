#include <stdio.h>
#include <string.h>

char PrintHello(char name[])
{
	printf("Hello! %s\n", name);
	// return 0;
}

struct Employee
{
	char name[100];
	int id;
	char roll[100];
	char office[100];
};

int main(int argc, char const *argv[])
{
	printf("This is a C program that contains a revision of all that I have learned till now\n");
	int fav_num = 65;
	char nameFistLetter = 'S';
	char FullName[50] = "Sannidhya Dasgupta";
	float decimal = 456.657;
	long VeryLong = 1234567775;
	printf("%d\n", fav_num);
	printf("%c\n", nameFistLetter);
	printf("%s\n", FullName);
	printf("%.3f\n", decimal);
	printf("%d\n", VeryLong);

	int rolls[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	for (int i = 0; i < 10; i++)
	{
		printf("%d\n", rolls[i]);
	}
	int i = 0;
	while (i < 11)
	{
		printf("%d\n", i);
		++i;
	}

	char hello = PrintHello("Sannidhya");
	// printf("%s\n", hello);
	struct Employee rajesh = {"Rajesh Khanna", 1, "Data Analyzer", "15/2 South Avenue, Black Forest Centers, New York City "};
	// "15/2 South Avenue, Black Forest Centers, New York City "};

	printf("The name is %s\n", rajesh.name);
	printf("The id is %d\n", rajesh.id);
	printf("The roll is %s\n", rajesh.roll);
	printf("The office address is %s\n", rajesh.office);
	return 0;
}