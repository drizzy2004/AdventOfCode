import re
def find_all_pairs(file_name):
    with open(file_name, "r") as file:
        text = file.read()

        pattern = r"mul\(\d+,\d+\)"

        matches = re.findall(pattern, text)

        return matches
    
def extract_numbers(arr):
    all_numbers = []
    for problem in arr:
        numbers = r"\d+,\d+"

        mul = re.findall(numbers, problem)
        all_numbers.append(mul)

    return all_numbers

def perform_operations(arr):
    result = sum(int(a) * int(b) for sublist in arr for a, b in [sublist[0].split(",")])
    return result
    
matches = find_all_pairs("sequence.txt")
all_numbers = extract_numbers(matches)
print(perform_operations(all_numbers))
