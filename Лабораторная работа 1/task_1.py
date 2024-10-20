numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_number_index = 4
sum_ = sum(numbers[:missing_number_index]) + sum(numbers[missing_number_index+1:])
numbers[missing_number_index] = sum_ / len(numbers)

print("Измененный список:", numbers)
