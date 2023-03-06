from breadFirst import bfs_8puzzle
from depthFirst import dfs_8puzzle
from heuristics import hamming_distance, manhattan_distance, permutation_inversion, linear_conflict
from bestFirst import best_first_search
from astar import astar
import time

start_state = [
    [2, 8, 3],
    [1, "", 4],
    [7, 6, 5]
]

# start_state = [    
#     [3, 6, 4],
#     ["", 1, 2],
#     [8, 7, 5]
# ]

goal_state = [
    [1, 2, 3],
    [8, "", 4],
    [7, 6, 5]
]

# Verifying BFS and DFS 
#print(bfs_8puzzle(start_state, goal_state))
#print(dfs_8puzzle(start_state, goal_state, [start_state]))

# Veryfing is heuristics are correct
#print(hamming_distance(start_state, goal_state))
#print(manhattan_distance(start_state, goal_state))
#print(permutation_inversion(start_state, goal_state))
#print(linear_conflict(start_state, goal_state))

heuristics = [hamming_distance, manhattan_distance, permutation_inversion, linear_conflict]

for heuristic in heuristics:
    # Best-First
    start_time = time.time()
    length, solution = best_first_search(start_state, goal_state, heuristic)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    print(f"Heuristic: {heuristic}")
    print(f"Time taken for best-first: {time_taken} milliseconds")
    print(f"Length of paths is: {length}")

    # A*
    start_time = time.time()
    length, solution = astar(start_state, goal_state, heuristic)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    print(f"Time taken for A*: {time_taken} milliseconds")
    print(f"Length of paths is: {length}")



