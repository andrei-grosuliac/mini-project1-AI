import heapq

def best_first_search(start_state, heuristic_fn):
    frontier = [(heuristic_fn(start_state), start_state)]
    explored = set()

    while frontier:
        _, state = heapq.heappop(frontier)
        if state.is_solved():
            return state
        explored.add(state)

        for successor in state.get_successors():
            if successor not in explored:
                heapq.heappush(frontier, (heuristic_fn(successor), successor))

    return None

def astar_search(start_state, heuristic_fn):
    frontier = [(0 + heuristic_fn(start_state), 0, start_state)]
    explored = set()

    while frontier:
        _, g, state = heapq.heappop(frontier)
        if state.is_solved():
            return state
        explored.add(state)

        for successor in state.get_successors():
            if successor not in explored:
                heapq.heappush(frontier, (g + heuristic_fn(successor), g+1, successor))

    return None