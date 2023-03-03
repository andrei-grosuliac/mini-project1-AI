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