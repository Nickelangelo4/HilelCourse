input_list1 = [1, 2, 3, 4, 5, 6]
input_list2 = [1, 2, 3]
input_list3 = [1, 2, 3, 4, 5]
input_list4 = [1]
input_list5 = []

input_list = input_list1
middle_index = (len(input_list) + 1) // 2 if input_list else 0
result = [input_list[:middle_index], input_list[middle_index:]]

print(result)