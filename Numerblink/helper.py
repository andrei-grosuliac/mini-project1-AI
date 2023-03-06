def get_adjacent_cells(x, y, width, height):
    """
    Get the cells adjacent to the given cell.

    :param x: The x-coordinate of the cell.
    :param y: The y-coordinate of the cell.
    :param width: The width of the puzzle.
    :param height: The height of the puzzle.
    :return: A list of the adjacent cells as (x, y) tuples.
    """
    adjacent_cells = []
    if x > 0:
        adjacent_cells.append((x - 1, y))
    if x < width - 1:
        adjacent_cells.append((x + 1, y))
    if y > 0:
        adjacent_cells.append((x, y - 1))
    if y < height - 1:
        adjacent_cells.append((x, y + 1))
    return adjacent_cells