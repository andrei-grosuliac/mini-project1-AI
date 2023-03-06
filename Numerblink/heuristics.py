from helper import get_adjacent_cells

def manhattan_distance_heuristic(state):
    """
    Compute the Manhattan distance between each endpoint pair in the state.

    :param state: The state of the puzzle.
    :return: The sum of the Manhattan distances between each endpoint pair.
    """
    endpoint_positions = {}
    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            if isinstance(cell, int):
                if cell in endpoint_positions:
                    endpoint_positions[cell].append((x, y))
                else:
                    endpoint_positions[cell] = [(x, y)]

    distance = 0
    for endpoints in endpoint_positions.values():
        distance += abs(endpoints[0][0] - endpoints[1][0]) + abs(endpoints[0][1] - endpoints[1][1])
    return distance

def intersection_count_heuristic(state):
    """
    Count the number of pairs of segments that intersect in the state.

    :param state: The state of the puzzle.
    :return: The number of pairs of intersecting segments.
    """
    intersection_count = 0
    segments = []
    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            if isinstance(cell, str):
                segments.append((cell, x, y))

    for i, (seg1, x1, y1) in enumerate(segments):
        for seg2, x2, y2 in segments[i + 1:]:
            if seg1 != seg2:
                if (x1, y1) in get_adjacent_cells(x2, y2) or (x2, y2) in get_adjacent_cells(x1, y1):
                    intersection_count += 1

    return intersection_count