def create_grid(file_name):
    with open(file_name, "r") as file:
        grid = file.read().splitlines()
    return grid

def count_words(grid):
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "X": continue
            for dir_row in [-1, 0, 1]:
                for dir_col in [-1, 0, 1]:
                    if dir_row == dir_col == 0:
                        continue
                    if not (0 <= r + 3 * dir_row < len(grid) and 0 <= c + 3 * dir_col < len(grid[0])): 
                        continue
                    if grid[r + dir_row][c + dir_col] == "M" and grid[r + 2 * dir_row][c + 2 * dir_col] == "A" and grid[r + 3 * dir_row][c + 3 * dir_col] == "S":
                        count += 1
    return count

grid = create_grid("word_search.txt")     
print(count_words(grid))                   