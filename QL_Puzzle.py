import random
import copy
# 2, 1 and 0 in order are representing sun, moon and blank.
source_puzzle = [[2, 2, 2],
                 [1, 2, 1],
                 [1, 0, 1]]
goal_puzzle = [[0, 1, 2],
               [1, 2, 1],
               [2, 1, 2]]
moves = ['U', 'R', 'D', 'L']
start = [[0, 1, 1], [1, 1, 2], [2, 2, 2]]
end = [[2, 2, 2], [2, 1, 1], [1, 1, 0]]
def state_to_number(state):
    number = 0
    for i in range(3):
        for j in range(3):
            number += 3**((8 - (i*3 + j))) * state[i][j]
    return number

def number_to_state(number):
    state = [[0, 0, 0] for i in range(3)]
    for i in range(3):
        for j in range(3):
            state[i][j] = number // 3**(8 - (i*3 + j))
            number %= 3**(8 - (i*3 + j))
    return state
    
# checks whether the move is legal or not
def check_move(state, move):
    for i in range(3):
        if (state[i][0] == 0 and move == 'L'):
            return False
        if (state[0][i] == 0 and move == 'U'):
            return False
        if (state[2][i] == 0 and move == 'D'):
            return False
        if (state[i][2] == 0 and move == 'R'):
            return False
    return True

def legal_moves(state):
    legal_m = []
    for i in moves:
        if check_move(state, i):
            legal_m.append(i)
    return legal_m

# we need to check_move before using def move
def next_state(state, move):
    new_state = copy.deepcopy(state)
    for i in range(3):
        for j in range(3):
            if new_state[i][j] == 0:
                break
        else: 
            continue
        break
    if move == "U":
        new_state[i][j] = new_state[i-1][j]
        new_state[i-1][j] = 0
    if move == "R":
        new_state[i][j] = new_state[i][j+1]
        new_state[i][j+1] = 0
    if move == "D":
        new_state[i][j] = new_state[i+1][j]
        new_state[i+1][j] = 0
    if move == "L":
        new_state[i][j] = new_state[i][j-1]
        new_state[i][j-1] = 0
    return new_state
def max_move(state):
    num_state = state_to_number(state)
    max_q = 0
    max_m = ""
    for i in table:
        if (i[0] == num_state and i[2] >= max_q):
            max_q = i[2]
            max_m = i[1]
    return max_m
def count_q(state, move):
    new_q = 0
    r = 0
    max = 0
    next = next_state(state, move)
    if next == goal_puzzle:
        r = 1
    number = state_to_number(next)
    for i in table:
        if (i[0] == number and i[2] > max):
            max = i[2]
    number = state_to_number(state)
    for i in table:
        if (i[0] == number and i[1] == move):
            old_q = i[2]
            break
    new_q = 0.9 * old_q + 0.1 * (r + 0.9 * max)
    i[2] = new_q
    # if (new_q != 0):
    #     print(state, move)
    #     print(new_q)
# now we are going to make the table from [[0, 1, 1], [1, 1, 2], [2, 2, 2]] that equals to 3320 to
# [[2, 2, 2], [2, 1, 1], [1, 1, 0]] that equals to 19560 each one with four moves from ['U', 'R', 'D', 'L']
table = []
for i in range(3320, 19561):
    for j in ['U', 'R', 'D', 'L']:
        two = 0
        one = 0
        for t in number_to_state(i):
            two += t.count(2)
            one += t.count(1)
        if ((two == 4) and (one == 4)):
            table.append([i, j, 0])
# we name [i, j, r] the Q, and we just work with them.
# new Q(s,a) = (1 - alpha)Q(s,a) + alpha(r + lambda * max(Q(s, a*)))
# alpha = 0.1, lambda = 0.9
for i in range(200):
    state = copy.deepcopy(source_puzzle)
    legal_m = legal_moves(state)
    rand = random.randint(0, len(legal_m) - 1)
    move = legal_m[rand]
    count_q(state, move)
    for j in range(500):
        # print(state, move)
        state = next_state(state, move)
        legal_m = legal_moves(state)
        # print(moves[(moves.index(move) + 2) % 4])
        legal_m.remove(moves[(moves.index(move) + 2) % 4])
        rand = random.randint(0, len(legal_m) - 1)
        move = legal_m[rand]
        count_q(state, move)
z = 0
for i in table:
    print_state = [['', '', ''] for i in range(3)]
    if (i[0] != z):
        z = i[0]
        state_print = number_to_state(z)
        for x in range(3):
            for y in range(3):
                if (state_print[x][y] == 0):
                    print_state[x][y] = "    "
                elif (state_print[x][y] == 1):
                    print_state[x][y] = "moon"
                elif (state_print[x][y] == 2):
                    print_state[x][y] = "sun "
            print(print_state[x])
        print(i[1], " = ", i[2])
    elif (x != 0):
        print(i[1], " = ", i[2])
current_state = copy.deepcopy(source_puzzle)
currernt_number = state_to_number(current_state)
while (current_state != goal_puzzle):
    print_state = [['', '', ''] for i in range(3)]
    for i in range(3):
        for j in range(3):
            if (current_state[i][j] == 0):
                print_state[i][j] = "    "
            elif (current_state[i][j] == 1):
                print_state[i][j] = "moon"
            elif (current_state[i][j] == 2):
                print_state[i][j] = "sun "
        print(print_state[i])
    print()
    move = max_move(current_state)
    current_state = next_state(current_state, move)
for i in range(3):
    for j in range(3):
        if (current_state[i][j] == 0):
            print_state[i][j] = "    "
        elif (current_state[i][j] == 1):
            print_state[i][j] = "moon"
        elif (current_state[i][j] == 2):
            print_state[i][j] = "sun "
    print(print_state[i])
print()