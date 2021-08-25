# Qlearning-Puzzle
## Algorithm
In this homework we are supposed to solve a problem and fill the Q-table using the Q-learning algorithm.
### The algorithm is :
	new Q(s,a) = (1 - alpha)Q(s,a) + alpha(r + lambda * maxQ(s', a'))
#### new Q(s,a) : updated amount for this cell of the table
#### alpha : for percentage of update that we want in each episod
#### Q(s,a) : old amount for this cell of the table
#### r : reward, that is 1 for the final-state (goal_puzzle), and 0 for other states
#### lambda : shows the weight of future rewards compared to current reward
#### maxQ(s',a') : maximum of all possible actions of "next" state (named future reward)

### Problem
The problem is about reaching to a final-state (goal_puzzle) from an initial-state (source-puzzle).
Our task is to roam in the state and try to reach the goal, and meanwhile filling the Q-table.

### Q-table
Eeach state (puzzle) consists of 4 suns, 4 moons and one empty cell.
we have 2, 1 and 0 in order for sun, moon and empty cell.
Q-table cells are a combination of state and move ("U", "R", "D", "L").
we have state and for each state we have 2, 3 or 4 moves.
our task is to fill the Q-table using Q-learning algorithm.

### CODE
### Functions
- state_to_number : we assign a number to each state, we put each array in a row 
and consider it as a number in mod 3, the purpose is to make the table (list) easier.

- number_to_state : reverse of previous function.

- check_move : it checks whether the move is legal for the state or not, based on this
fact that only when empty cell is in middle we have 4 legal moves and other situations
there are at most 3 or 2 legal moves.

- legal_moves : gives a list of legal moves for each state using "check_move" function.


- next_state : this returns next state (state + move --> next_state).

- count_q : updates Q-table cell using the algorithm ( old_q <-- new_q ).

### Body
We start to make the table from 3320 (that stands for [[0, 1, 1], [1, 1, 2], [2, 2, 2]] in mod 3) to 
19560 (that stands for [[2, 2, 2], [2, 1, 1], [1, 1, 0]] in mod 3) and only for states that have 
four suns (2) and four moons (1) and one empty cell (0), because obviously numbers between this two
number can also generate somthing that is not in our problem. (like 5 suns or etc...)
for each standard number (state) we have 4 moves (we don't omit illegal moves and just leave them 0)
so we will have 630 * 4 cells in our table.
also each cell has it's Q, so number, move("U", "R", "D", "L"), Q(between zero to 1))
Then we start 200 episods starting from source_puzzle and each one with 500 random moves.
also keep in mind that for legal moves from each state we delete the move that brings us back to the 
previous state.
in the rest of the code we try to print the output as you can see a part of it below
