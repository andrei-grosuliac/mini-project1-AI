from searchHelper import get_successors, is_goal

def bfs_8puzzle(start_state, goal_state):
    open_list = [start_state]
    closed_list = []   
    
    while open_list:
        # Get the next state from the Open list
        current_state = open_list.pop(0)
        # Check if the state is the goal state
        if is_goal(current_state, goal_state):
            return current_state
        # Generate the successor states
        successors = get_successors(current_state)
        # Add the successor states to the Open list
        for successor in successors:
            if successor not in closed_list and successor not in open_list:
                open_list.append(successor)
        # Add the current state to the Closed list
        closed_list.append(current_state)
        
    # If the algorithm reaches this point, there is no solution
    return "There is no solution"