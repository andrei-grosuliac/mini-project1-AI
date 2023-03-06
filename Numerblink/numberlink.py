class NumberlinkPuzzle:
    def __init__(self, grid, links):
        self.grid = grid
        self.links = links

    def is_solved(self):
        for link in self.links:
            for i in range(len(link)-1):
                row1, col1 = link[i]
                row2, col2 = link[i+1]
                if self.grid[row1][col1] != self.grid[row2][col2]:
                    return False
        return True

    def get_successors(self):
        for link_idx, link in enumerate(self.links):
            if all(self.grid[row][col] != '.' for row, col in link):
                continue  # link is already complete
            link_values = set(self.grid[row][col] for row, col in link) | ({"|" if link[0][1] == link[1][1] else "-"} - set('.'))
            for value in link_values:
                new_grid = [row.copy() for row in self.grid]
                for row, col in link:
                    new_grid[row][col] = value
                yield NumberlinkPuzzle(new_grid, self.links)

    def __str__(self):
        link_coords = set(coord for link in self.links for coord in link)
        s = ""
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if (row_idx, col_idx) in link_coords:
                    s += str(cell)
                elif cell == ".":
                    s += "."
                else:
                    s += " "
                if col_idx < len(row) - 1 and ((row_idx, col_idx+1) in link_coords or (row_idx, col_idx) in link_coords):
                    s += "-"
            if row_idx < len(self.grid) - 1:
                s += "\n"
                for col_idx, cell in enumerate(row):
                    if (row_idx, col_idx) in link_coords and (row_idx+1, col_idx) in link_coords:
                        s += "|"
                    else:
                        s += " "
                    s += " "
                    if col_idx == len(row) - 1 or (row_idx, col_idx+1) not in link_coords:
                        s += " "
                s += "\n"
        return s.strip()

    def __repr__(self):
        return f"NumberlinkPuzzle(grid={self.grid}, links={self.links})"