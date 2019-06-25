#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - a non stop loop
 * input: VOID
 * Return: 0 on success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - entry point
 * Return: 0 on success
 */
int main(void)
{
	pid_t p_1 = 0, p_2 = 0, p_3 = 0, p_4 = 0, p_5 = 0;

	p_1 = fork();
	if (p_1 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}

	p_2 = fork();
	if (p_2 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	p_3 = fork();
	if (p_3 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}

	p_4 = fork();
	if (p_4 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
	p_5 = fork();
	if (p_5 == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}

	infinite_while();
	return (0);
}
