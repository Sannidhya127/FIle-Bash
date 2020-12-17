#include <windows.h>
#include <stdio.h>
#include <conio.h>
#include <unistd.h>
// #include <graphics.h>

int main()
{
	printf("\n\n\t\tStudytonight - Best place to learn\n\n\n");

	//BACKGROUND_RED| BACKGROUND_GREEN| BACKGROUND_BLUE| BACKGROUND_INTENSITY

	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), BACKGROUND_RED);
	printf("\n\nIsn't this Awesome?");
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), BACKGROUND_INTENSITY | BACKGROUND_RED);
	printf("\n\nYou just did something that only 1 out of 10 coders are familiar of :)\n");
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), BACKGROUND_GREEN | BACKGROUND_INTENSITY);
	printf("\n\nYou are doing great!!");
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), BACKGROUND_BLUE | BACKGROUND_INTENSITY);
	printf("\n\nThe best is yet to come!");
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), BACKGROUND_GREEN | BACKGROUND_INTENSITY);
	printf("\n\nWhat are you waiting for?? Just play with it!!");
	printf("\n\n\t\t\tCoding is Fun !\n\n\n");

	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), BACKGROUND_GREEN | BACKGROUND_INTENSITY);
	printf("\n\nThis is super");
	sleep(5);
	// SetTextColor(hdc, 4);
	// int *hdc;
	// SetTextColor(hdc, RGB(255, 0, 0));
	// _cprintf("C programming");

	// getch();

	return 0;
}