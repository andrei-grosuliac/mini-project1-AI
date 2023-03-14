from Numerblink.numberlink import NumberlinkPuzzle


start_grid = [
    [1, 2, 3, 4],
    [2, ".", ".", "."],
    [3, ".", ".", "."],
    [4, ".", ".", "."]D
]

links = []

x = NumberlinkPuzzle(start_grid, links)
print(x)
while x.is_solved == False:
    x = x.get_successors()

print(x)
