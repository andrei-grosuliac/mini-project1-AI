from priorityQueue import PriorityQueue
from searchHelper import get_successors

def best_first_search(start_state, goal_state, heuristic):
    visited = []
    pq = PriorityQueue()
    pq.put(heuristic(start_state, goal_state), start_state)
    while not pq.empty():
        state = pq.get()
        if state == goal_state:
            return state
        visited.append(state)
        for successor in get_successors(state):
            if successor not in visited:
                pq.put(heuristic(successor, goal_state), successor)
    return None
