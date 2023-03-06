# Define the possible moves
moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    
# Define a function to get the successor states of a state
def get_successors(state):
    successors = []
    i, j = get_blank_index(state)
    for move, (di, dj) in moves.items():
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            successors.append(new_state)
    return successors

# Define a function to get the index of the blank space in a state
def get_blank_index(state):
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            if value == "":
                return (i, j)

# Checks if a state is the goal state
def is_goal(state, goal_state):
    return state == goal_state

# Helper function to find coordinates of a specific number
def find_location(n, state):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == n:
                return i, j

# Covnert 2D to 1D array to facilitate the permuation inversion calculations
def flatten(l):
    return [item for sublist in l for item in sublist]