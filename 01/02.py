lst = [0, 12, 0, 5, 3]
non_zero_elements = [x for x in lst if x != 0]
zero_count = lst.count(0)
result = non_zero_elements + [0] * zero_count
print(result)