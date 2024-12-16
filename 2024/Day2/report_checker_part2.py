def check_reports(file_path):
    safe_reports = 0
    
    def remove_single_element(numbers):
        for i in range(len(numbers)):
            sublist = numbers[:i] + numbers[i+1:]  # Exclude the i-th element
            
            # Check conditions for increase
            increase = 0
            for j in range(len(sublist) - 1):
                if sublist[j] < sublist[j + 1]:
                    increase += 1

            if (increase == len(sublist) - 1):
                if all(abs(sublist[j] - sublist[j + 1]) > 0 and abs(sublist[j] - sublist[j + 1]) <= 3 
                       for j in range(len(sublist) - 1)):
                    return True

            # Check conditions for decrease
            decrease = 0
            for j in range(len(sublist) - 1):
                if sublist[j] > sublist[j + 1]:
                    decrease += 1

            if (decrease == len(sublist) - 1):
                if all(abs(sublist[j] - sublist[j + 1]) > 0 and abs(sublist[j] - sublist[j + 1]) <= 3 
                       for j in range(len(sublist) - 1)):
                    return True

        return False

    with open(file_path, "r") as file:
        for line in file:
            # Convert the line into a list of numbers
            numbers = list(map(int, line.split()))
            
            if remove_single_element(numbers):
                safe_reports += 1

    return safe_reports

print(check_reports("reports.txt"))
