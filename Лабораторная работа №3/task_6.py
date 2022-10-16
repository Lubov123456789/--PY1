list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


max_element = 0
low_element = list_numbers[len(list_numbers) - 1]
max = list_numbers[0]
for i in range(len(list_numbers)):

    current_max = list_numbers[i]
    if current_max > max:
        max, max_element = current_max, i


list_numbers[len(list_numbers) - 1] = max
list_numbers[max_element] = low_element
print(list_numbers)
