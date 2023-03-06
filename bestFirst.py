from priorityQueue import PriorityQueue
from searchHelper import get_successors

def best_first_search(start_state, goal_state, heuristic):
    visited = []
    visited.append(start_state)
    pq = PriorityQueue()
    pq.put(heuristic(start_state, goal_state), start_state)
    parent = {tuple(map(tuple, start_state)): None}

    # Start the search
    while not pq.empty():
        current  = pq.get()
        #print(heuristic)
        # Check if the current state is the goal state
        if current == goal_state:
            # Build the path by following the parent pointers
            path = []
            while current:
                path.append(current)
                current = parent[tuple(map(tuple, current))]
            path.reverse()
            return len(path)-1, path # Return path length and path
        
        # Generate the successors of the current state and add them to the priority queue if they haven't been visited
        for successor in get_successors(current):
            if successor not in visited:
                visited.append(successor)
                parent[tuple(map(tuple, successor))] = current
                pq.put(heuristic(successor, goal_state), successor)
    # If the goal state is not found, return None
    return None, None
