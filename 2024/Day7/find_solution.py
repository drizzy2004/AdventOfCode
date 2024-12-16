with open("equations.txt", "r") as file:

    part_1 = 0
    part_2 = 0

    for line in file:
        result, numbers = line.split(":")
        # print(result)
        # print(numbers)
        result = int(result)
        numbers = list(map(int, numbers.split()))
        # print(numbers) 

        # Here we solve for part 1

        previous_results = {numbers[0]}
        for next_number in numbers[1:]:
            previous_results = {r for prev in previous_results for r in (prev+next_number, prev*next_number) if r <= result}
        
        if result in previous_results:
            part_1 += result
            part_2 += result
            continue


        previous_results = {numbers[0]}
        for next_number in numbers[1:]:
            previous_results = {r for prev in previous_results for r in (prev+next_number, prev*next_number, int(f"{prev}{next_number}")) if r <= result}
        if result in previous_results:
            part_2 += result




print("Part1 Solution: ", part_1)
print("Part2 Solution: ", part_2)


