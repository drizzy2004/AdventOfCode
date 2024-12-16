from collections import defaultdict

# Parse input from the file
with open("rules.txt") as file:
    raw_rules, updates = file.read().strip().split("\n\n")
    rules = []
    for line in raw_rules.split("\n"):
        a, b = line.split("|")
        rules.append((int(a), int(b)))
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

# Function to check if an update follows all rules
def follows_rules(update, rules):
    index = {num: i for i, num in enumerate(update)}
    for a, b in rules:
        if a in index and b in index and index[a] >= index[b]:
            return False  # Rule violation found
    return True  # No rule violations

# Function to fix updates so they follow the rules
def fix_updates(update, rules):
    while True:
        is_sorted = True
        for i in range(len(update) - 1):
            if (update[i + 1], update[i]) in rules:
                update[i], update[i + 1] = update[i + 1], update[i]
                is_sorted = False
        if is_sorted:  # Terminate when no swaps are made
            break
    return update

# Main logic
solution = 0
for update in updates:
    if follows_rules(update, rules):
        continue
    # Fix updates and calculate the midpoint value
    seq = fix_updates(update, rules)
    solution += seq[len(seq) // 2]

print("Solution:", solution)
