def extract_list(column, file_path):
    first_list = []

    with open(file_path, "r") as file:
        for line in file:
            first_list.append(line.split()[column])

    first_list = [int(num) for num in first_list]

    return first_list


list1 = extract_list(0, "lists.txt")
list2 = extract_list(1, "lists.txt")

total = 0
for i in range(len(list1)):  # Iterate through indices of list1
    number = list1[i]       # Current number in list1
    count = 0               # Reset count for this number
    for element in list2:   # Check all elements in list2
        if element == number:  # Match found
            count += 1         # Increment count
    total += (number * count)  # Add total contribution for this number

print(total) 





    



