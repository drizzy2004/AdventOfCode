def check_bounds(xy, bounds):
    return 0 <= xy[0] < bounds[0] and 0 <= xy[1] < bounds[1]


antennas = dict()
with open("antennas.txt", "r") as file:
    all_lines = file.read().splitlines()

bounds = (len(all_lines[0]), len(all_lines))
for y, line in enumerate(all_lines):
    for x, char in enumerate(line):
        if char != ".":
            antennas.setdefault(char, []).append((x, y))

antinodes_1 = set()
antinodes_2 = set()


for type in antennas:
    for i, a in enumerate(antennas[type]):
        for b in antennas[type][i + 1:]:
            xDiff, yDiff = b[0] - a[0], b[1] - a[1]

            # Here we solve for part 1
            if check_bounds(outsideA := (a[0] - xDiff, a[1] - yDiff), bounds):
                antinodes_1.add(outsideA)
            if check_bounds(outsideB := (b[0] + xDiff, b[1] + yDiff), bounds):
                antinodes_1.add(outsideB)

            # Here we solve for part 2
            i = 0
            while check_bounds(outsideA := (a[0] - xDiff*i, a[1] - yDiff*i), bounds):
                antinodes_2.add(outsideA)
                i += 1
            i = 0
            while check_bounds(outsideB := (b[0] + xDiff*i, b[1] + yDiff*i), bounds):
                antinodes_2.add(outsideB)
                i += 1


print("Part 1 Solution: ", len(antinodes_1))
print("Part 2 Solution: ", len(antinodes_2))