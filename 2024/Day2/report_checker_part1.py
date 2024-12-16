def check_reports(file_path):
    count_increase = 0
    count_decrease = 0
    with open(file_path, "r") as file:
        for line in file:
            # Convert the line into a list of numbers
            numbers = list(map(int, line.split()))

            increase = 0
            decrease = 0
            
            # Compare elements in the list
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    decrease += 1  # Example comparison, increment count if current number is greater than the next
                elif numbers[i] < numbers[i + 1]:
                    increase += 1

            if (increase == (len(numbers) - 1)):
                if all(abs(numbers[j] - numbers[j + 1]) > 0 and abs(numbers[j] - numbers[j + 1]) <= 3 for j in range(len(numbers) - 1)):
                    count_increase += 1
            
            if (decrease == (len(numbers) - 1)):
                if all(abs(numbers[j] - numbers[j + 1]) > 0 and abs(numbers[j] - numbers[j + 1]) <= 3 for j in range(len(numbers) - 1)):
                    count_decrease += 1
                
    

    return count_increase + count_decrease
                

print(check_reports("reports.txt"))