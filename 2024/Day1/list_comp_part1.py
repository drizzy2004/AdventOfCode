def selection_sort(arr):
    # Traverse through all list elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted portion
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


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
for i in range(len(list1)):
    difference = abs(selection_sort(list1)[i] - selection_sort(list2)[i])
    total += difference

print(total)




    



