% N-Queens Problem in MiniZinc

% Include the global constraints library
include "globals.mzn";

% Define the size of the board (N x N)
int: N;

% Decision variable: q[i] represents the column of the queen in row i
array[1..N] of var 1..N: q;

% Constraints to ensure that no two queens threaten each other
constraint
    % Ensure no two queens are in the same column
    all_different(q) /\
    
    % Ensure no two queens are in the same diagonal (difference of rows and columns)
    all_different([q[i] + i | i in 1..N]) /\
    all_different([q[i] - i | i in 1..N]);

% Solve the problem
solve satisfy;

% Output the solution as a list of queen positions
output [ show(q) ];
