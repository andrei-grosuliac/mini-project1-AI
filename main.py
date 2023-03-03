from breadFirst import bfs_8puzzle
from depthFirst import dfs_8puzzle
from heuristics import hamming_distance, manhattan_distance, permutation_inversion
from bestFirst import best_first_search
from astar import astar

start_state = [
    [2, 8, 3],
    [1, "", 4],
    [7, 6, 5]
]

goal_state = [
    [1, 2, 3],
    [8, "", 4],
    [7, 6, 5]
]
heuristic = manhattan_distance
#solution = best_first_search(start_state, goal_state, heuristic)
solution = astar(start_state, goal_state, heuristic)
#solution = bfs_8puzzle(start_state, goal_state)
#solution = dfs_8puzzle(start_state, goal_state, [start_state])
print(solution)
#print(hamming_distance(start_state, goal_state))
#print(manhattan_distance(start_state, goal_state))
#print(permutation_inversion(start_state, goal_state))

