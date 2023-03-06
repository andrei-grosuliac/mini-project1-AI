from searchHelper import flatten, find_location

# Hamming distance heuristic
def hamming_distance(state, goal_state):
    distance = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j] != goal_state[i][j] and state[i][j] != "":
                distance += 1
    return distance

# Manhattan distance heuristic
def manhattan_distance(state, goal_state):
    distance = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j] != "":
                x, y = find_location(state[i][j], goal_state)
                distance += abs(i - x) + abs(j - y)
    return distance

# Permutation Inversion heuristic
def permutation_inversion(state, goal_state):
    state_list = flatten(state)
    goal_list = flatten(goal_state)
    state_inv = count_inversions(state_list)
    goal_inv = count_inversions(goal_list)
    return abs(state_inv - goal_inv)

# Counting the permutations inversions
def count_inversions(lst):
    inversions = 0
    n = len(lst)
    for i in range(n):
        if lst[i] == "":
            continue
        for j in range(i+1, n):
            if lst[j] == "":
                continue
            if lst[i] > lst[j]:
                inversions += 1
    return inversions

def linear_conflict(state, goal_state):

    # Step 2: Compute the number of linear conflicts in each row and column
    h_linear = 0
    for i in range(3):
        row_conflicts = 0
        col_conflicts = 0
        for j in range(3):
            tile1 = state[i][j]
            if tile1 != "":
                goal_row1, goal_col1 = find_location(tile1, goal_state)
                if goal_row1 == i:
                    for k in range(j+1, 3):
                        tile2 = state[i][k]
                        if tile2 != "":
                            goal_row2, goal_col2 = find_location(tile2, goal_state)
                            if goal_row2 == i and goal_col1 > goal_col2:
                                row_conflicts += 1
                if goal_col1 == j:
                    for k in range(i+1, 3):
                        tile2 = state[k][j]
                        if tile2 != "":
                            goal_row2, goal_col2 = find_location(tile2, goal_state)
                            if goal_col2 == j and goal_row1 > goal_row2:
                                col_conflicts += 1
        h_linear += row_conflicts + col_conflicts

    # Step 3: Add the combined Manhattan Distance and linear conflicts to get the total heuristic value
    return manhattan_distance(state, goal_state) + 2 * h_linear