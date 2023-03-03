from searchHelper import get_successors, is_goal

def dfs_8puzzle(state, goal_state, visited):

    # Check if the state is the goal state
    if is_goal(state, goal_state):
        return state
    # Generate the successor states
    successors = get_successors(state)
    # Visit each successor state recursively
    for successor in successors:
        if successor not in visited:
            visited.append(successor)
            result = dfs_8puzzle(successor, goal_state, visited)
            if result is not None:
                return result
    return None