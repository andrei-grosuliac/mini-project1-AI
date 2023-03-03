from priorityQueue import PriorityQueue
from searchHelper import get_successors

def astar(start_state, goal_state, heuristic):

    # Define the initial state and priority queue
    pq = PriorityQueue()
    pq.put(heuristic(start_state, goal_state), start_state)
    parent = {tuple(map(tuple, start_state)): None}
    cost = {tuple(map(tuple, start_state)): 0}

    # Search until the queue is empty or the goal is found
    while not pq.empty():

        # Get the next state with the lowest f-score
        current = pq.get()

        # Check if the goal state has been reached
        if current == goal_state:
            path = []
            while current:
                path.append(current)
                current = parent[tuple(map(tuple, current))]
            path.reverse()
            return path

        # Generate and process the successors of the current state
        for successor in get_successors(current):
            new_cost = cost[tuple(map(tuple, current))] + 1
            if tuple(map(tuple, successor)) not in cost or new_cost < cost[tuple(map(tuple, successor))]:
                cost[tuple(map(tuple, successor))] = new_cost
                priority = new_cost + heuristic(successor, goal_state)
                pq.put(priority, successor)
                parent[tuple(map(tuple, successor))] = current

    # If the queue is empty, the goal was not found
    return None