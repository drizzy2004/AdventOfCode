import re

def find_all_valid_pairs(file_name):
    if file_name:
        with open(file_name, "r") as file:
            text = file.read()
    elif text is None:
        raise ValueError("Either text or file_name must be provided.")

    total = 0
    process = True

    for expr in re.findall(r"(don\'t\(\)|do\(\)|mul\(\d+,\d+\))", text):
        if expr == "don't()":
            process = False
        elif expr == "do()":
            process = True
        elif process:
            L, R = re.findall(r"\d+", expr)
            total += int(L) * int(R)

    print(total)

# Example Usage
print(find_all_valid_pairs("sequence.txt"))
