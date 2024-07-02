# 0x05. N Queens

This project is part of the Algorithm Python curriculum. The goal is to solve the classic N Queens problem using backtracking algorithms in Python. Then i will enhance the performance by leveraging C code and using it as a shared library in Python.

## Concepts Needed:

- **Backtracking Algorithms**: Understand how to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
- **Recursion**: Implement backtracking algorithms using recursive functions.
- **List Manipulations in Python**: Create and manipulate lists to store the positions of queens on the board.
- **Python Command Line Arguments**: Handle command-line arguments with the sys module.
- **Interfacing C with Python**: Use C for performance-critical code and integrate it with Python using shared libraries.

## Steps:

### 1. Write the C File

I started by writing the C code to solve the N Queens problem. The C code includes functions for solving the problem using backtracking, adding solutions, checking if a position is safe, and printing solutions.

**Example C Code:**

```c
/* 0-nqueens.c */

#include <stdio.h>
#include <stdlib.h>

/* Function declarations */
void solve_nqueens(int size);
void solve_nqueens_util(int **board, int size, int col, int ***solutions, int *solution_count);
void add_solution(int **board, int size, int ***solutions, int *solution_count);
int is_safe(int **board, int size, int row, int col);
void print_solutions(int **solutions, int solution_count, int size);

```

### 2. Compile the C Code into a Shared Library

Next, compile the C code into a shared library that can be used in Python.

```sh
gcc -shared -o libnqueens.so -fPIC 0-nqueens.c
```

### 3. Create the Python Script to Use the Shared Library

Then create a Python script that uses the shared library to solve the N Queens problem. This script initializes the shared library, and provides a class to interface with the shared library.

**Example Python Code:**

```python
#!/usr/bin/python3

import ctypes
import sys

class NQueensSolver:
    def __init__(self, size: int) -> None:
        self.size = size
        self.lib = ctypes.CDLL("./libnqueens.so")
```

### 4. Run the Python Script

Finally, you can run the Python script with the desired board size to solve the N Queens problem.

```sh
./0-nqueens_so.py 8
```

This setup allows you to leverage the performance of C for solving the N Queens problem while providing the convenience of a Python interface.

## Performance Insights

I conducted a performance comparison between the Python script and the Python script with the shared library. Here are the results for N=10:

- Average execution time for `0-nqueens.py`: **820.00 milliseconds**
- Average execution time for `0-nqueens_so.py`: **30.00 milliseconds**

As demonstrated, the Python script with the shared library significantly outperforms the pure Python script, showcasing the efficiency of C for performance-critical code.
