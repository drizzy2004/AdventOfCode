with open("rules.txt") as file:
    raw_rules, updates = file.read().strip().split("\n\n")
    rules = []
    for line in raw_rules.split("\n"):
        a, b = line.split("|")
        rules.append((int(a), int(b)))
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

def follows_rules(update):
    index = {}
    for i, num in enumerate(update):
        index[num] = i

    for a, b in rules:
        if a in index and b in index and not index[a] < index[b]:
            return False, 0
    return True, update[len(update) // 2]


solution = 0
for update in updates:
    good, mid = follows_rules(update)
    if good:
        solution += mid

print(solution)


