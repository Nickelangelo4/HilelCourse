lst = [12, 3, 4, 9]
result = lst[-1:] + lst[:-1] if len(lst) > 1 else lst
print(result)