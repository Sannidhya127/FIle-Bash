#include <stdio.h>
#include <stdlib.h>
// #include <graphics.h>
#include <conio.h>
// !Star patter n programm in C Language made by Sannidhya Dasgupta
void starPattern(int rows)
{
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			printf("*");
		}
		printf("\n");
	}
}

void reverseStarPattern(int rows)
{
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j <= rows - i; j++)
		{
			printf("*");
		}
		printf("\n");
	}
}

int main(int argc, char const *argv[])
{
	/* Start Pattern Ex */
	textcolor(4); // You could type "4" instead of "RED", but it is not as readable
	printf("Hello, World!");

	// getch();
	int rows, opt, numW = 10;
	// int w = true;
	int x;
	for (x = 0; x = 10; x = x + 1)
	{
		printf("Please enter 0 for non-reversed triangular star pattern and 1 for reversed triangular star pattern and 5 to exit\n");
		scanf("%d", &opt);
		switch (opt)
		{
		case 0:
			printf("[38;5;46mC: How many rows do you want: [0m");
			scanf("%d", &rows);
			starPattern(rows);
			break;

		case 1:
			printf("How many rows do you want: ");
			scanf("%d", &rows);
			reverseStarPattern(rows);
			break;
		case 5:
			exit(0);

		default:
			printf("Your input is invalid!\n");
			break;
			exit(0);
		}
	}

	return 0;
}
