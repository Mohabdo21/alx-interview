#include <stdio.h>
#include <stdlib.h>

void solve_nqueens(int size);
void solve_nqueens_util(int **board, int size, int col, int ***solutions,
		int *solution_count);
int is_safe(int **board, int size, int row, int col);
void print_solutions(int **solutions, int solution_count, int size);

/**
 * main - Main function to handle command line arguments and start the solver
 * @argc: Argument count
 * @argv: Argument vector
 * Return: 0 on success, 1 on failure
 */
int main(int argc, char **argv)
{
	int n;

	if (argc != 2)
	{
		printf("Usage: nqueens N\n");
		return (1);
	}

	n = atoi(argv[1]);
	if (n < 4)
	{
		printf("N must be at least 4\n");
		return (1);
	}

	solve_nqueens(n);

	return (0);
}

/**
 * solve_nqueens - Solves the N Queens problem
 * @size: The size of the board (the number of queens)
 */
void solve_nqueens(int size)
{
	int **board;
	int **solutions = NULL;
	int solution_count = 0;
	int i, j;

	board = malloc(size * sizeof(int *));
	for (i = 0; i < size; i++)
	{
		board[i] = malloc(size * sizeof(int));
		for (j = 0; j < size; j++)
			board[i][j] = 0;
	}

	solve_nqueens_util(board, size, 0, &solutions, &solution_count);
	print_solutions(solutions, solution_count, size);

	for (i = 0; i < size; i++)
		free(board[i]);
	free(board);

	for (i = 0; i < solution_count; i++)
		free(solutions[i]);
	free(solutions);
}

/**
 * solve_nqueens_util - Utilizes backtracking to solve the N Queens problem
 * @board: Double pointer to the 2D array representing the chessboard
 * @size: The size of the board (the number of queens)
 * @col: The current column
 * @solutions: Triple pointer to store the solutions
 * @solution_count: Pointer to the solution count
 *
 * This function uses a recursive backtracking algorithm to solve the N Queens
 * problem. It places a queen in a column, then recursively calls itself to
 * place queens in the next columns. If a safe position is found, it marks
 * this cell in the board and moves to the next column. If no safe position
 * can be found in the current column or if the queen placed in the previous
 * column leads to no solution, then it backtracks and returns false.
 */
void solve_nqueens_util(int **board, int size, int col, int ***solutions,
		int *solution_count)
{
	int i, j, **new_solutions;

	if (col >= size)
	{
		new_solutions = malloc((*solution_count + 1) * sizeof(int *));
		for (i = 0; i < *solution_count; i++)
			new_solutions[i] = (*solutions)[i];

		new_solutions[*solution_count] = malloc(size * 2 * sizeof(int));
		for (i = 0; i < size; i++)
			for (j = 0; j < size; j++)
				if (board[i][j] == 1)
				{
					new_solutions[*solution_count][i * 2] = i;
					new_solutions[*solution_count][i * 2 + 1] = j;
				}

		free(*solutions);
		*solutions = new_solutions;
		(*solution_count)++;
		return;
	}

	for (i = 0; i < size; i++)
	{
		if (is_safe(board, size, i, col))
		{
			board[i][col] = 1;
			solve_nqueens_util(board, size, col + 1, solutions, solution_count);
			board[i][col] = 0;
		}
	}
}

/**
 * is_safe - Checks if it's safe to place a queen at board[row][col]
 * @board: Double pointer to the 2D array representing the chessboard
 * @size: The size of the board (the number of queens)
 * @row: The current row
 * @col: The current column
 * Return: 1 if it's safe, 0 otherwise
 *
 * This function checks if a queen can be placed at board[row][col] without
 * being attacked by any other queen. It checks the left side of the row,
 * the upper-left diagonal, and the lower-left diagonal for any queens.
 */
int is_safe(int **board, int size, int row, int col)
{
	int i, j;

	for (i = 0; i < col; i++)
		if (board[row][i])
			return (0);

	for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
		if (board[i][j])
			return (0);

	for (i = row, j = col; j >= 0 && i < size; i++, j--)
		if (board[i][j])
			return (0);

	return (1);
}

/**
 * print_solutions - Prints all the solutions
 * @solutions: Double pointer to the solutions
 * @solution_count: The solution count
 * @size: The size of the board (the number of queens)
 */
void print_solutions(int **solutions, int solution_count, int size)
{
	int i, j;

	for (i = 0; i < solution_count; i++)
	{
		printf("[");
		for (j = 0; j < size; j++)
		{
			printf("[%d, %d]", solutions[i][j * 2], solutions[i][j * 2 + 1]);
			if (j < size - 1)
				printf(", ");
		}
		printf("]\n");
	}
}
